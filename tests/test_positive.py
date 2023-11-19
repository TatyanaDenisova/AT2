import subprocess

tst = "/home/user/txt"
out = "/home/user/out"
folder = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1 create archive files to archive
    result1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(out), "arx2.7z")
    assert result1 and result2, "test1 FAIL"


def test_step2():
    # test2 output from archive
    result1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder), "iiii")
    result3 = checkout("cd {}; ls".format(folder), "pppp")
    result4 = checkout("cd {}; ls".format(folder), "rrrr")
    assert result1 and result2 and result3 and result4, "test2 FAIL"


def test_step3():
    # test3 full archive
    assert checkout("cd {}; 7z t arx2.7z".format(out), "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4 renew archive
    assert checkout("cd {}; 7z u {}/arx2.7z".format(tst, out), "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5 del files from archive
    assert checkout("cd {}; 7z d arx2.7z".format(out), "Everything is Ok"), "test5 FAIL"


def test_step6():
    assert checkout("cd {}; 7z l arx2.7z".format(out), "Listing archive"), "test6 FAIL"


def test_step7():
    result1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder), "iiii")
    result3 = checkout("cd {}; ls".format(folder), "pppp")
    result4 = checkout("cd {}/rrrr; ls".format(folder), "ssss")
    result5 = checkout("cd {}/rrrr; ls".format(folder), "www")
    assert result1 and result2 and result3 and result4, "test7 FAIL"
