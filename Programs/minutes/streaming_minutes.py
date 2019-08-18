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
