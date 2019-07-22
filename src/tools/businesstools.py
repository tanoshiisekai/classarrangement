from tools.info import Info


def analysetimestr(astr):
    totalsectionlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    sectionlist = []
    if "!" in astr:
        validlist = []
        week, section = astr.split("!")
        if section == "*":
            validlist = totalsectionlist
        else:
            sectionlist = section.split(",")
            for tsec in totalsectionlist:
                if tsec not in sectionlist:
                    validlist.append(tsec)
        if week == "*":
            return {
                "一": validlist,
                "二": validlist,
                "三": validlist,
                "四": validlist,
                "五": validlist
            }
        else:
            if "," in week:
                resultdict = {}
                weeklist = week.split(",")
                for week in weeklist:
                    resultdict.update({week: validlist})
                return resultdict
            else:
                return {
                    week: validlist
                }
    if "@" in astr:
        validlist = []
        week, section = astr.split("@")
        if section == "*":
            validlist = totalsectionlist
        else:
            sectionlist = section.split(",")
            validlist = sectionlist
        if week == "*":
            return {
                "一": validlist,
                "二": validlist,
                "三": validlist,
                "四": validlist,
                "五": validlist
            }
        else:
            if "," in week:
                resultdict = {}
                weeklist = week.split(",")
                for week in weeklist:
                    resultdict.update({week: validlist})
                return resultdict
            else:
                return {
                    week: validlist
                }


def availabletimetodict(availablestr):
    """
    print(businesstools.availabletimetodict("一!1,2#二@*#三@1,2,6,7#四,五!5,6,7"))
    print(businesstools.availabletimetodict("*@1,2,3,4"))
    print(businesstools.availabletimetodict("*!1,2,5,6"))
    """
    # 注意：如果星期用星号，则代表每天都一样；否则，星期只能明确指明星期几
    # @表示有效的节次
    # !表示排除的节次
    # 多个节次或多个星期用,隔开
    resultdict = {}
    if "#" in availablestr:
        # 分星期几处理
        availablelist = availablestr.split("#")
        for astr in availablelist:
            if astr[0] == "*":
                return Info(infostatus=False, infomsg="非法的时间节次字符串！")
            else:
                resultdict.update(analysetimestr(astr))
    else:
        # 每天都一样
        resultdict.update(analysetimestr(availablestr))
    return resultdict


def availabletimetolist(availablestr):
    totalsectionlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    resultdict = availabletimetodict(availablestr)
    resultlist = []
    for key, value in resultdict.items():
        for ts in totalsectionlist:
            if ts in value:
                resultlist.append((key, ts, True))
            else:
                resultlist.append((key, ts, False))
    return resultlist

