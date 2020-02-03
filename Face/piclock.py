from tkinter import *
import tkinter.ttk as ttk
import os
import requests
import json
import math
from PIL import Image, ImageTk
from datetime import datetime, timedelta

# OpenWeatherMap の情報
KEY = "********************************"
ZIP = "101-0032,JP"
URL = "http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}"

# メインウィンドウ作成
root = Tk()

# メインウィンドウサイズ
root.geometry("1024x768")

# メインウィンドウタイトル
root.title("Clock")

# MainFrame クラス
class MainFrame(ttk.Frame):
    # コンストラクタ
    def __init__(self, master=None, **kwargs):
        # 親クラスのコンストラクタを呼び出す
        super().__init__(master, **kwargs)

        # create_widgets を呼び出す
        self.create_widgets()

    # ウィジェットを作成
    def create_widgets(self):
        # フレームを作成
        self.frame=Frame(self, bg="white", bd=0, height=460, relief="flat")

        # 時刻表示（配置は直接指定）
        self.wt=Label(self.frame, text="", bg="white", font=("", 160))
        self.wt.place(width=884, x=60, y=120)

        # 日付表示（配置は直接指定）
        self.wd=Label(self.frame, text="", bg="white", font=("", 60, "bold"))
        self.wd.place(width=744, x=160, y=60)

        # 地域表示（左寄せ）
        self.wp=Label(self.frame, text="", bg="white", fg="gray", font=("", 20, "bold"), anchor="w")
        self.wp.place(width=920, x=42, y=440)

        # フレームを配置
        self.frame.grid(row=0, column=0, columnspan=8, sticky="news")

        # このスクリプトの絶対パス
        self.scr_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        # 天候アイコン（ディクショナリ）
        self.icon_dict={
            "01d":Image.open(self.scr_path + "/img/01d.png"), "01n":Image.open(self.scr_path + "/img/01n.png"),
            "02d":Image.open(self.scr_path + "/img/02d.png"), "02n":Image.open(self.scr_path + "/img/02n.png"),
            "03d":Image.open(self.scr_path + "/img/03.png"),  "03n":Image.open(self.scr_path + "/img/03.png"),
            "04d":Image.open(self.scr_path + "/img/04.png"),  "04n":Image.open(self.scr_path + "/img/04.png"),
            "09d":Image.open(self.scr_path + "/img/09.png"),  "09n":Image.open(self.scr_path + "/img/09.png"),
            "10d":Image.open(self.scr_path + "/img/10.png"),  "10n":Image.open(self.scr_path + "/img/10.png"),
            "11d":Image.open(self.scr_path + "/img/11.png"),  "11n":Image.open(self.scr_path + "/img/11.png"),
            "13d":Image.open(self.scr_path + "/img/13.png"),  "13n":Image.open(self.scr_path + "/img/13.png"),
            "50d":Image.open(self.scr_path + "/img/50.png"),  "50n":Image.open(self.scr_path + "/img/50.png")
        }

        # アイコンサイズを画面サイズにフィット（64x64）させる
        for key, value in self.icon_dict.items():
            self.icon_dict[key]=self.icon_dict[key].resize((64, 64), Image.ANTIALIAS)
            self.icon_dict[key]=ImageTk.PhotoImage(self.icon_dict[key])

        # 天気予報（時間帯）
        self.wwl=[
            Label(self, text="3",  bg="white", font=("", 30, "bold")),
            Label(self, text="6",  bg="white", font=("", 30, "bold")),
            Label(self, text="9",  bg="white", font=("", 30, "bold")),
            Label(self, text="12", bg="white", font=("", 30, "bold")),
            Label(self, text="15", bg="white", font=("", 30, "bold")),
            Label(self, text="18", bg="white", font=("", 30, "bold")),
            Label(self, text="21", bg="white", font=("", 30, "bold")),
            Label(self, text="24", bg="white", font=("", 30, "bold"))
        ]

        # 天気予報（時間帯）を配置
        for i in range(len(self.wwl)):
            self.wwl[i].grid(row=1, column=i, sticky="news")

        # 天気予報（天候）
        self.wwi=[
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white"),
            Label(self, image=self.icon_dict["01d"], bg="white")
        ]

        # 天気予報（天候）を配置
        for i in range(len(self.wwi)):
            self.wwi[i].grid(row=2, column=i, sticky="news")

        # 天気予報（気温）
        self.wwt=[
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20)),
            Label(self, text="０°C", bg="white", font=("", 20))
        ]

        # 天気予報（気温）を配置
        for i in range(len(self.wwt)):
            self.wwt[i].grid(row=3, column=i, sticky="news")

        # 天気予報（降水量）
        self.wwr=[
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20)),
            Label(self, text="０mm", bg="white", font=("", 20))
        ]

        # 天気予報（降水量）を配置
        for i in range(len(self.wwr)):
            self.wwr[i].grid(row=4, column=i, sticky="news")

        # レイアウト
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        for i in range(len(self.wwl)):
            self.columnconfigure(i, weight=1)

# メインフレームを配置
app=MainFrame(root)
app.pack(side=TOP, expand=1, fill=BOTH)

# メインウィンドウを閉じる
def wm_close():
    root.destroy()

# 閉じるボタン作成
btn=Button(root, text=" X ", font=('', 16), relief=FLAT, command=wm_close)

# 画面がリサイズされたとき
def change_size(event):
    # ボタンの位置を右上に
    btn.place(x=root.winfo_width() - 60, y=14)

# 画面のリサイズをバインドする
root.bind('<Configure>', change_size)

# メインウィンドウの最大化
#root.attributes("-zoom", "1")
root.attributes("-fullscreen", "1")

# 常に最前面に表示
root.attributes("-topmost", True)

def update_time():
    # 現在日時を表示
    now=datetime.now()
    d="{0:0>4d}/{1:0>2d}/{2:0>2d} ({3}.)".format(now.year, now.month, now.day, now.strftime("%a"))
    t="{0:0>2d}:{1:0>2d}:{2:0>2d}".format(now.hour, now.minute, now.second)
    app.wd.configure(text=d)
    app.wt.configure(text=t)

    # 1秒間隔で繰り返す
    root.after(1000, update_time)

# 初回起動
update_time()

def update_weather():
    # 表示カウンタ
    count=0

    # URL を作成して OpenWeatherMap に問い合わせを行う
    url=URL.format(ZIP, KEY)
    response=requests.get(url)
    forecastData=json.loads(response.text)

    # 結果が得られない場合は即時終了
    if not ("list" in forecastData):
        print("error")
        return

    # デバッグ用
    print(forecastData)

    # 結果を 3 時間単位で取得
    for item in forecastData["list"]:
        # 時間帯を 24 時間表記で表示
        forecastDatetime = datetime.fromtimestamp(item["dt"])
        app.wwl[count].configure(text=forecastDatetime.hour)

        # 気候をアイコンで表示
        app.wwi[count].configure(image=app.icon_dict[item["weather"][0]["icon"]])

        # 気温を表示
        app.wwt[count].configure(text="{0}°c".format(round(item["main"]["temp"])))

        # 降水量を表示
        rainfall = 0
        if "rain" in item and "3h" in item["rain"]:
            rainfall = item["rain"]["3h"]
        app.wwr[count].configure(text="{0}mm".format(math.ceil(rainfall)))

        # 表示カウンタを更新
        count += 1

        # 全て表示し終えたらループ終了
        if count >= len(app.wwl):
            # 地域情報を表示
            app.wp.configure(text="{0}, {1} (lat:{2}, lon:{3})".format(
                forecastData["city"]["country"],
                forecastData["city"]["name"],
                forecastData["city"]["coord"]["lat"],
                forecastData["city"]["coord"]["lon"]))

            # 60 秒間隔で繰り返す
            root.after(60000, update_weather)

            return

# 初回起動
update_weather()

# コールバック関数を登録
root.after(1000,  update_time)
root.after(60000, update_weather)

# メインループ
root.mainloop()
