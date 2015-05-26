TEAMS_CONFERENCE_AND_DIVISION = 'json_callback({  "headers": [\'team\', \' conference\', \' division\'], "groups": [ {    "sdql": "season = 2014" ,   "columns" : [     [\'Seahawks\',\'Packers\',\'Bears\',\'Bills\',\'Broncos\',\'Colts\',\'Buccaneers\',\'Panthers\',\'Chiefs\',\'Titans\',\'Cowboys\',\'Fortyniners\',\'Dolphins\',\'Patriots\',\'Eagles\',\'Jaguars\',\'Falcons\',\'Saints\',\'Jets\',\'Raiders\',\'Rams\',\'Vikings\',\'Ravens\',\'Bengals\',\'Steelers\',\'Browns\',\'Texans\',\'Redskins\',\'Cardinals\',\'Chargers\',\'Lions\',\'Giants\'],     [\'NFC\',\'NFC\',\'NFC\',\'AFC\',\'AFC\',\'AFC\',\'NFC\',\'NFC\',\'AFC\',\'AFC\',\'NFC\',\'NFC\',\'AFC\',\'AFC\',\'NFC\',\'AFC\',\'NFC\',\'NFC\',\'AFC\',\'AFC\',\'NFC\',\'NFC\',\'AFC\',\'AFC\',\'AFC\',\'AFC\',\'AFC\',\'NFC\',\'NFC\',\'AFC\',\'NFC\',\'NFC\'],     [\'NFC West\',\'NFC North\',\'NFC North\',\'AFC East\',\'AFC West\',\'AFC South\',\'NFC South\',\'NFC South\',\'AFC West\',\'AFC South\',\'NFC East\',\'NFC West\',\'AFC East\',\'AFC East\',\'NFC East\',\'AFC South\',\'NFC South\',\'NFC South\',\'AFC East\',\'AFC West\',\'NFC West\',\'NFC North\',\'AFC North\',\'AFC North\',\'AFC North\',\'AFC North\',\'AFC South\',\'NFC East\',\'NFC West\',\'AFC West\',\'NFC North\',\'NFC East\',]   ]}   ] });\n'
TEAMS_CONFERENCE_AND_DIVISION_SOLUTION = {"Bears":{"conference":"NFC","division":"NFC North"},"Bengals":{"conference":"AFC","division":"AFC North"},"Bills":{"conference":"AFC","division":"AFC East"},"Broncos":{"conference":"AFC","division":"AFC West"},"Browns":{"conference":"AFC","division":"AFC North"},"Buccaneers":{"conference":"NFC","division":"NFC South"},"Cardinals":{"conference":"NFC","division":"NFC West"},"Chargers":{"conference":"AFC","division":"AFC West"},"Chiefs":{"conference":"AFC","division":"AFC West"},"Colts":{"conference":"AFC","division":"AFC South"},"Cowboys":{"conference":"NFC","division":"NFC East"},"Dolphins":{"conference":"AFC","division":"AFC East"},"Eagles":{"conference":"NFC","division":"NFC East"},"Falcons":{"conference":"NFC","division":"NFC South"},"Fortyniners":{"conference":"NFC","division":"NFC West"},"Giants":{"conference":"NFC","division":"NFC East"},"Jaguars":{"conference":"AFC","division":"AFC South"},"Jets":{"conference":"AFC","division":"AFC East"},"Lions":{"conference":"NFC","division":"NFC North"},"Packers":{"conference":"NFC","division":"NFC North"},"Panthers":{"conference":"NFC","division":"NFC South"},"Patriots":{"conference":"AFC","division":"AFC East"},"Raiders":{"conference":"AFC","division":"AFC West"},"Rams":{"conference":"NFC","division":"NFC West"},"Ravens":{"conference":"AFC","division":"AFC North"},"Redskins":{"conference":"NFC","division":"NFC East"},"Saints":{"conference":"NFC","division":"NFC South"},"Seahawks":{"conference":"NFC","division":"NFC West"},"Steelers":{"conference":"AFC","division":"AFC North"},"Texans":{"conference":"AFC","division":"AFC South"},"Titans":{"conference":"AFC","division":"AFC South"},"Vikings":{"conference":"NFC","division":"NFC North"}}
TEAMS_SCHEDULE_AND_OPPONENT = 'json_callback({  "headers": [\'date\', \' o:team\'], "groups": [ {    "sdql": "team = Colts and season = 2014" ,   "columns" : [     [20140907,20140915,20140921,20140928,20141005,20141009,20141019,20141026,20141103,20141116,20141123,20141130,20141207,20141214,20141221,20141228,20150104,20150111,20150118],     [\'Broncos\',\'Eagles\',\'Jaguars\',\'Titans\',\'Ravens\',\'Texans\',\'Bengals\',\'Steelers\',\'Giants\',\'Patriots\',\'Jaguars\',\'Redskins\',\'Browns\',\'Texans\',\'Cowboys\',\'Titans\',\'Bengals\',\'Broncos\',\'Patriots\']   ]}   ] });\n'
TEAMS_SCHEDULE_AND_OPPONENT_SOLUTION = {20140907:{"opponent":"Broncos"},20140915:{"opponent":"Eagles"},20140921:{"opponent":"Jaguars"},20140928:{"opponent":"Titans"},20141005:{"opponent":"Ravens"},20141009:{"opponent":"Texans"},20141019:{"opponent":"Bengals"},20141026:{"opponent":"Steelers"},20141103:{"opponent":"Giants"},20141116:{"opponent":"Patriots"},20141123:{"opponent":"Jaguars"},20141130:{"opponent":"Redskins"},20141207:{"opponent":"Browns"},20141214:{"opponent":"Texans"},20141221:{"opponent":"Cowboys"},20141228:{"opponent":"Titans"},20150104:{"opponent":"Bengals"},20150111:{"opponent":"Broncos"},20150118:{"opponent":"Patriots"}}