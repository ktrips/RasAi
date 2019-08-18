 def make_minutes(convs):
       conv_title= "打ち合わせ"
       conv_cont = ""
       minutes_temp={
            "title":"議題：",
            "date":"日付：",
            "written":"作成者：",
            "contents":"議事内容："
       }
       dateStr = datetime.now().strftime('%Y-%m-%d')
       for con in convs:
           convTimeStr = con["convDateTime"].strftime('%H:%M:%S')
           if con["keyw"] in ["minutes"]:
               conv_title = con["convt"]
           conv_cont += '(' + str(con["number"]) +') ' + con["convt"] + ' (' + convTimeStr + ')\n'
       minutes = minutes_temp["title"] + conv_title + '\n'
       minutes+= minutes_temp["date"] + dateStr + '\n'
       minutes+= minutes_temp["written"] + mail + '\n'
       minutes+= minutes_temp["contents"] + '\n' + conv_cont
       subject = conv_title + '(' + dateStr + ')'
       return subject, minutes


# (def main()プログラム中)
         if not text:
           print('Sorry but please say again in ' + speech_lang)
         else:
           convDateStr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           i += 1
           print(str(i) + text + convDateStr)
           minutes_words= ['議事録', '打合せ', 'ミーティング']
           keyw = ""
           text.lower()
           for m in minutes_words:
             if text.find(m) > -1:
               keyw = "minutes"
               break
           conv = {"number": i,
               "convDateTime": datetime.now(),
               "convt": text,
               "keyw": keyw}
           convs.append(conv)
           if repeat != "no":

            
           bye_words    = ['終わりです', '終了', 'おわり', 'さようなら', 'さよなら', 'バイバイ']
…
               aiy.audio.say(nolang, "en-US")
           if text in bye_words:
             subject, minutes = make_minutes(convs)
             if mail:
               os.system('echo "' + minutes + '" | mail -s "' + subject + '" ' + mail)
             break
           time.sleep(0.2)



if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('--speech', dest='speech_lang', type=str, default='', help='Base speech language')
   parser.add_argument('--repeat', dest='repeat', type=str, default='speech', help='Repeat the speech or not')
   parser.add_argument('--mail', dest='mail', type=str, default='', help='send to email')
   args   = parser.parse_args()
   speech_lang= args.speech_lang if args.speech_lang else default_speech
   repeat = args.repeat if args.repeat else "speech"
   mail   = args.mail if args.mail else ''
   main()
