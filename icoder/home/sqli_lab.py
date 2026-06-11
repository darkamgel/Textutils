"""Intentionally vulnerable SQL endpoints for security scanner / training lab."""
from django.db import connection
from django.http import HttpResponse

def sqli_001(request):
    sql = "SELECT sno FROM blog_post WHERE title = '" + request.GET.get("p1", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_001:{len(rows)}")

def sqli_002(request):
    sql = "SELECT sno FROM blog_post WHERE title LIKE '%" + request.GET.get("p2", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_002:{len(rows)}")

def sqli_003(request):
    sql = "SELECT * FROM blog_post WHERE title = '" + request.GET.get("p3", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_003:{len(rows)}")

def sqli_004(request):
    sql = "SELECT COUNT(*) FROM blog_post WHERE title = '" + request.GET.get("p4", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_004:{len(rows)}")

def sqli_005(request):
    sql = "SELECT sno FROM blog_post WHERE title = '" + request.GET.get("p5", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_005:{len(rows)}")

def sqli_006(request):
    sql = "SELECT sno FROM blog_post WHERE title != '" + request.GET.get("p6", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_006:{len(rows)}")

def sqli_007(request):
    sql = "SELECT sno FROM blog_post WHERE title = '" + request.GET.get("p7", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_007:{len(rows)}")

def sqli_008(request):
    sql = "SELECT sno FROM blog_post WHERE LOWER(title) = LOWER('" + request.GET.get("p8", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_008:{len(rows)}")

def sqli_009(request):
    sql = "SELECT sno FROM blog_post WHERE content = '" + request.GET.get("p9", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_009:{len(rows)}")

def sqli_010(request):
    sql = "SELECT sno FROM blog_post WHERE content LIKE '%" + request.GET.get("p10", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_010:{len(rows)}")

def sqli_011(request):
    sql = "SELECT * FROM blog_post WHERE content = '" + request.GET.get("p11", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_011:{len(rows)}")

def sqli_012(request):
    sql = "SELECT COUNT(*) FROM blog_post WHERE content = '" + request.GET.get("p12", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_012:{len(rows)}")

def sqli_013(request):
    sql = "SELECT sno FROM blog_post WHERE content = '" + request.GET.get("p13", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_013:{len(rows)}")

def sqli_014(request):
    sql = "SELECT sno FROM blog_post WHERE content != '" + request.GET.get("p14", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_014:{len(rows)}")

def sqli_015(request):
    sql = "SELECT sno FROM blog_post WHERE content = '" + request.GET.get("p15", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_015:{len(rows)}")

def sqli_016(request):
    sql = "SELECT sno FROM blog_post WHERE LOWER(content) = LOWER('" + request.GET.get("p16", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_016:{len(rows)}")

def sqli_017(request):
    sql = "SELECT sno FROM blog_post WHERE author = '" + request.GET.get("p17", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_017:{len(rows)}")

def sqli_018(request):
    sql = "SELECT sno FROM blog_post WHERE author LIKE '%" + request.GET.get("p18", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_018:{len(rows)}")

def sqli_019(request):
    sql = "SELECT * FROM blog_post WHERE author = '" + request.GET.get("p19", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_019:{len(rows)}")

def sqli_020(request):
    sql = "SELECT COUNT(*) FROM blog_post WHERE author = '" + request.GET.get("p20", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_020:{len(rows)}")

def sqli_021(request):
    sql = "SELECT sno FROM blog_post WHERE author = '" + request.GET.get("p21", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_021:{len(rows)}")

def sqli_022(request):
    sql = "SELECT sno FROM blog_post WHERE author != '" + request.GET.get("p22", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_022:{len(rows)}")

def sqli_023(request):
    sql = "SELECT sno FROM blog_post WHERE author = '" + request.GET.get("p23", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_023:{len(rows)}")

def sqli_024(request):
    sql = "SELECT sno FROM blog_post WHERE LOWER(author) = LOWER('" + request.GET.get("p24", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_024:{len(rows)}")

def sqli_025(request):
    sql = "SELECT sno FROM blog_post WHERE slug = '" + request.GET.get("p25", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_025:{len(rows)}")

def sqli_026(request):
    sql = "SELECT sno FROM blog_post WHERE slug LIKE '%" + request.GET.get("p26", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_026:{len(rows)}")

def sqli_027(request):
    sql = "SELECT * FROM blog_post WHERE slug = '" + request.GET.get("p27", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_027:{len(rows)}")

def sqli_028(request):
    sql = "SELECT COUNT(*) FROM blog_post WHERE slug = '" + request.GET.get("p28", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_028:{len(rows)}")

def sqli_029(request):
    sql = "SELECT sno FROM blog_post WHERE slug = '" + request.GET.get("p29", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_029:{len(rows)}")

def sqli_030(request):
    sql = "SELECT sno FROM blog_post WHERE slug != '" + request.GET.get("p30", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_030:{len(rows)}")

def sqli_031(request):
    sql = "SELECT sno FROM blog_post WHERE slug = '" + request.GET.get("p31", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_031:{len(rows)}")

def sqli_032(request):
    sql = "SELECT sno FROM blog_post WHERE LOWER(slug) = LOWER('" + request.GET.get("p32", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_032:{len(rows)}")

def sqli_033(request):
    sql = "SELECT sno FROM home_contact WHERE name = '" + request.GET.get("p33", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_033:{len(rows)}")

def sqli_034(request):
    sql = "SELECT sno FROM home_contact WHERE name LIKE '%" + request.GET.get("p34", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_034:{len(rows)}")

def sqli_035(request):
    sql = "SELECT * FROM home_contact WHERE name = '" + request.GET.get("p35", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_035:{len(rows)}")

def sqli_036(request):
    sql = "SELECT COUNT(*) FROM home_contact WHERE name = '" + request.GET.get("p36", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_036:{len(rows)}")

def sqli_037(request):
    sql = "SELECT sno FROM home_contact WHERE name = '" + request.GET.get("p37", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_037:{len(rows)}")

def sqli_038(request):
    sql = "SELECT sno FROM home_contact WHERE name != '" + request.GET.get("p38", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_038:{len(rows)}")

def sqli_039(request):
    sql = "SELECT sno FROM home_contact WHERE name = '" + request.GET.get("p39", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_039:{len(rows)}")

def sqli_040(request):
    sql = "SELECT sno FROM home_contact WHERE LOWER(name) = LOWER('" + request.GET.get("p40", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_040:{len(rows)}")

def sqli_041(request):
    sql = "SELECT sno FROM home_contact WHERE email = '" + request.GET.get("p41", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_041:{len(rows)}")

def sqli_042(request):
    sql = "SELECT sno FROM home_contact WHERE email LIKE '%" + request.GET.get("p42", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_042:{len(rows)}")

def sqli_043(request):
    sql = "SELECT * FROM home_contact WHERE email = '" + request.GET.get("p43", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_043:{len(rows)}")

def sqli_044(request):
    sql = "SELECT COUNT(*) FROM home_contact WHERE email = '" + request.GET.get("p44", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_044:{len(rows)}")

def sqli_045(request):
    sql = "SELECT sno FROM home_contact WHERE email = '" + request.GET.get("p45", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_045:{len(rows)}")

def sqli_046(request):
    sql = "SELECT sno FROM home_contact WHERE email != '" + request.GET.get("p46", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_046:{len(rows)}")

def sqli_047(request):
    sql = "SELECT sno FROM home_contact WHERE email = '" + request.GET.get("p47", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_047:{len(rows)}")

def sqli_048(request):
    sql = "SELECT sno FROM home_contact WHERE LOWER(email) = LOWER('" + request.GET.get("p48", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_048:{len(rows)}")

def sqli_049(request):
    sql = "SELECT sno FROM home_contact WHERE phone = '" + request.GET.get("p49", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_049:{len(rows)}")

def sqli_050(request):
    sql = "SELECT sno FROM home_contact WHERE phone LIKE '%" + request.GET.get("p50", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_050:{len(rows)}")

def sqli_051(request):
    sql = "SELECT * FROM home_contact WHERE phone = '" + request.GET.get("p51", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_051:{len(rows)}")

def sqli_052(request):
    sql = "SELECT COUNT(*) FROM home_contact WHERE phone = '" + request.GET.get("p52", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_052:{len(rows)}")

def sqli_053(request):
    sql = "SELECT sno FROM home_contact WHERE phone = '" + request.GET.get("p53", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_053:{len(rows)}")

def sqli_054(request):
    sql = "SELECT sno FROM home_contact WHERE phone != '" + request.GET.get("p54", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_054:{len(rows)}")

def sqli_055(request):
    sql = "SELECT sno FROM home_contact WHERE phone = '" + request.GET.get("p55", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_055:{len(rows)}")

def sqli_056(request):
    sql = "SELECT sno FROM home_contact WHERE LOWER(phone) = LOWER('" + request.GET.get("p56", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_056:{len(rows)}")

def sqli_057(request):
    sql = "SELECT sno FROM home_contact WHERE content = '" + request.GET.get("p57", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_057:{len(rows)}")

def sqli_058(request):
    sql = "SELECT sno FROM home_contact WHERE content LIKE '%" + request.GET.get("p58", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_058:{len(rows)}")

def sqli_059(request):
    sql = "SELECT * FROM home_contact WHERE content = '" + request.GET.get("p59", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_059:{len(rows)}")

def sqli_060(request):
    sql = "SELECT COUNT(*) FROM home_contact WHERE content = '" + request.GET.get("p60", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_060:{len(rows)}")

def sqli_061(request):
    sql = "SELECT sno FROM home_contact WHERE content = '" + request.GET.get("p61", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_061:{len(rows)}")

def sqli_062(request):
    sql = "SELECT sno FROM home_contact WHERE content != '" + request.GET.get("p62", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_062:{len(rows)}")

def sqli_063(request):
    sql = "SELECT sno FROM home_contact WHERE content = '" + request.GET.get("p63", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_063:{len(rows)}")

def sqli_064(request):
    sql = "SELECT sno FROM home_contact WHERE LOWER(content) = LOWER('" + request.GET.get("p64", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_064:{len(rows)}")

def sqli_065(request):
    sql = "SELECT sno FROM blog_blogcomment WHERE comment = '" + request.GET.get("p65", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_065:{len(rows)}")

def sqli_066(request):
    sql = "SELECT sno FROM blog_blogcomment WHERE comment LIKE '%" + request.GET.get("p66", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_066:{len(rows)}")

def sqli_067(request):
    sql = "SELECT * FROM blog_blogcomment WHERE comment = '" + request.GET.get("p67", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_067:{len(rows)}")

def sqli_068(request):
    sql = "SELECT COUNT(*) FROM blog_blogcomment WHERE comment = '" + request.GET.get("p68", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_068:{len(rows)}")

def sqli_069(request):
    sql = "SELECT sno FROM blog_blogcomment WHERE comment = '" + request.GET.get("p69", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_069:{len(rows)}")

def sqli_070(request):
    sql = "SELECT sno FROM blog_blogcomment WHERE comment != '" + request.GET.get("p70", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_070:{len(rows)}")

def sqli_071(request):
    sql = "SELECT sno FROM blog_blogcomment WHERE comment = '" + request.GET.get("p71", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_071:{len(rows)}")

def sqli_072(request):
    sql = "SELECT sno FROM blog_blogcomment WHERE LOWER(comment) = LOWER('" + request.GET.get("p72", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_072:{len(rows)}")

def sqli_073(request):
    sql = "SELECT sno FROM auth_user WHERE username = '" + request.GET.get("p73", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_073:{len(rows)}")

def sqli_074(request):
    sql = "SELECT sno FROM auth_user WHERE username LIKE '%" + request.GET.get("p74", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_074:{len(rows)}")

def sqli_075(request):
    sql = "SELECT * FROM auth_user WHERE username = '" + request.GET.get("p75", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_075:{len(rows)}")

def sqli_076(request):
    sql = "SELECT COUNT(*) FROM auth_user WHERE username = '" + request.GET.get("p76", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_076:{len(rows)}")

def sqli_077(request):
    sql = "SELECT sno FROM auth_user WHERE username = '" + request.GET.get("p77", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_077:{len(rows)}")

def sqli_078(request):
    sql = "SELECT sno FROM auth_user WHERE username != '" + request.GET.get("p78", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_078:{len(rows)}")

def sqli_079(request):
    sql = "SELECT sno FROM auth_user WHERE username = '" + request.GET.get("p79", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_079:{len(rows)}")

def sqli_080(request):
    sql = "SELECT sno FROM auth_user WHERE LOWER(username) = LOWER('" + request.GET.get("p80", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_080:{len(rows)}")

def sqli_081(request):
    sql = "SELECT sno FROM auth_user WHERE email = '" + request.GET.get("p81", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_081:{len(rows)}")

def sqli_082(request):
    sql = "SELECT sno FROM auth_user WHERE email LIKE '%" + request.GET.get("p82", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_082:{len(rows)}")

def sqli_083(request):
    sql = "SELECT * FROM auth_user WHERE email = '" + request.GET.get("p83", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_083:{len(rows)}")

def sqli_084(request):
    sql = "SELECT COUNT(*) FROM auth_user WHERE email = '" + request.GET.get("p84", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_084:{len(rows)}")

def sqli_085(request):
    sql = "SELECT sno FROM auth_user WHERE email = '" + request.GET.get("p85", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_085:{len(rows)}")

def sqli_086(request):
    sql = "SELECT sno FROM auth_user WHERE email != '" + request.GET.get("p86", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_086:{len(rows)}")

def sqli_087(request):
    sql = "SELECT sno FROM auth_user WHERE email = '" + request.GET.get("p87", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_087:{len(rows)}")

def sqli_088(request):
    sql = "SELECT sno FROM auth_user WHERE LOWER(email) = LOWER('" + request.GET.get("p88", "") + "')"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_088:{len(rows)}")

def sqli_089(request):
    sql = "SELECT sno FROM auth_user WHERE first_name = '" + request.GET.get("p89", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_089:{len(rows)}")

def sqli_090(request):
    sql = "SELECT sno FROM auth_user WHERE first_name LIKE '%" + request.GET.get("p90", "") + "%'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_090:{len(rows)}")

def sqli_091(request):
    sql = "SELECT * FROM auth_user WHERE first_name = '" + request.GET.get("p91", "") + "' LIMIT 10"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_091:{len(rows)}")

def sqli_092(request):
    sql = "SELECT COUNT(*) FROM auth_user WHERE first_name = '" + request.GET.get("p92", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_092:{len(rows)}")

def sqli_093(request):
    sql = "SELECT sno FROM auth_user WHERE first_name = '" + request.GET.get("p93", "") + "' ORDER BY sno DESC"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_093:{len(rows)}")

def sqli_094(request):
    sql = "SELECT sno FROM auth_user WHERE first_name != '" + request.GET.get("p94", "") + "'"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_094:{len(rows)}")

def sqli_095(request):
    sql = "SELECT sno FROM auth_user WHERE first_name = '" + request.GET.get("p95", "") + "' OR 1=1"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
    return HttpResponse(f"sqli_095:{len(rows)}")

SQLI_VULN_VIEWS = [
    sqli_001,
    sqli_002,
    sqli_003,
    sqli_004,
    sqli_005,
    sqli_006,
    sqli_007,
    sqli_008,
    sqli_009,
    sqli_010,
    sqli_011,
    sqli_012,
    sqli_013,
    sqli_014,
    sqli_015,
    sqli_016,
    sqli_017,
    sqli_018,
    sqli_019,
    sqli_020,
    sqli_021,
    sqli_022,
    sqli_023,
    sqli_024,
    sqli_025,
    sqli_026,
    sqli_027,
    sqli_028,
    sqli_029,
    sqli_030,
    sqli_031,
    sqli_032,
    sqli_033,
    sqli_034,
    sqli_035,
    sqli_036,
    sqli_037,
    sqli_038,
    sqli_039,
    sqli_040,
    sqli_041,
    sqli_042,
    sqli_043,
    sqli_044,
    sqli_045,
    sqli_046,
    sqli_047,
    sqli_048,
    sqli_049,
    sqli_050,
    sqli_051,
    sqli_052,
    sqli_053,
    sqli_054,
    sqli_055,
    sqli_056,
    sqli_057,
    sqli_058,
    sqli_059,
    sqli_060,
    sqli_061,
    sqli_062,
    sqli_063,
    sqli_064,
    sqli_065,
    sqli_066,
    sqli_067,
    sqli_068,
    sqli_069,
    sqli_070,
    sqli_071,
    sqli_072,
    sqli_073,
    sqli_074,
    sqli_075,
    sqli_076,
    sqli_077,
    sqli_078,
    sqli_079,
    sqli_080,
    sqli_081,
    sqli_082,
    sqli_083,
    sqli_084,
    sqli_085,
    sqli_086,
    sqli_087,
    sqli_088,
    sqli_089,
    sqli_090,
    sqli_091,
    sqli_092,
    sqli_093,
    sqli_094,
    sqli_095,
]
