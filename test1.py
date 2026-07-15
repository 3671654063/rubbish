import sys
# 检查目录（字典不会用，暂且借鉴了下deepsleep）
# 1:检查常见危险目录
def fileaddress():
    word_dict = {}
    for idx, word in enumerate(words):
        if word not in word_dict:  # 只记录第一次
           word_dict[word] = idx
    print(word_dict)
    word_set = set(preset_words)
    keys_in_order = list(word_dict.keys())
    target_words = keys_in_order[this_word:]
    for word in target_words:
        if all(ch in word_set for ch in word):
            print(f"{word} ← 危险命令！！！")
        else:
            print(f"{word} ← 再看一眼，对吗（？）")

# 2:检查目录格式
def fuck_fileaddress():
    word_dict = {}
    for idx, word in enumerate(words):
        if word not in word_dict:  # 只记录第一次
           word_dict[word] = idx
    word_set = set(fuck_words)
    keys_in_order = list(word_dict.keys())
    target_words = keys_in_order[this_word:]
    for word in target_words:
        if word and word[0] in word_set:
            print(f"{word} ← 格式正确")
        else:
            print(f"{word} ← ！！！危险")

# 预处理
declaration = ("输入你的rm-rf命令")
mid = input(declaration)
words = mid.split( )
words_number = len(words)
if words_number <= 2:
    print("格式错误：词数不够")
    sys.exit()
try:
    first_words = words[0]
except IndexError:
    print("请输入文本")
    sys.exit()
if first_words == "sudo":
    testnumber = 1
else:
    testnumber = 0

# 单词位置
first_words = words[testnumber]
second_words = words[testnumber+1]
try:
    third_words = words[testnumber+2]
except IndexError:
    print("格式错误：词数不够")
    sys.exit()
# 预设地址
preset_words = ["/", "/bin", "/user/bin", "/user/sbin", "/sbin","/bin/sh", "/user/bin/sh", "/sbin/sh", "/usr/sbin/sh", "/usr/bin/sh", "/usr", "/usr/bin", "/usr/sbin" "/lib", "/lib64", "/libx64", "/lib32", "/libx32", "/lib/modules", "/lib64/modules", "/libx64/modules", "/lib32/modules", "/libx32/modules", "/etc", "/boot", "/boot/efi", "/efi",  "/proc", "/proc/sys", "/sys", "/run", "/var", "/root", "/home", "/opt", "/srv", "/usr/local", "/user/local", "/tmp", "/media", "/mnt", "/bin*", "/user/bin*", "/user/sbin*", "/sbin*","/bin/sh*", "/user/bin/sh*", "/sbin/sh*", "/usr/sbin/sh*", "/usr/bin/sh*", "/usr*", "/usr/bin*", "/usr/sbin*" "/lib*", "/lib64*", "/libx64*", "/lib32*", "/libx32*", "/lib/modules*", "/lib64/modules*", "/libx64/modules*", "/lib32/modules*", "/libx32/modules*", "/etc*", "/boot*", "/boot/efi*", "/efi*",  "/proc*", "/proc/sys*", "/sys*", "/run*", "/var*", "/root*", "/home*", "/opt*", "/srv*", "/usr/local*", "/user/local*", "/tmp*", "/media*", "/mnt*", "/bin/", "/user/bin/", "/user/sbin/", "/sbin/","/bin/sh/", "/user/bin/sh/", "/sbin/sh/", "/usr/sbin/sh/", "/usr/bin/sh/", "/usr/", "/usr/bin/", "/usr/sbin/" "/lib/", "/lib64/", "/libx64/", "/lib32/", "/libx32/", "/lib/modules/", "/lib64/modules/", "/libx64/modules/", "/lib32/modules/", "/libx32/modules/", "/etc/", "/boot/", "/boot/efi/", "/efi/",  "/proc/", "/proc/sys/", "/sys/", "/run/", "/var/", "/root/", "/home/", "/opt/", "/srv/", "/usr/local/", "/user/local/", "/tmp/", "/media/", "/mnt/", "/*", "/bin*/", "/user/bin/*", "/user/sbin/*", "/sbin/*","/bin/sh/*", "/user/bin/sh/*", "/sbin/sh/*", "/usr/sbin/sh/*", "/usr/bin/sh/*", "/usr/*", "/usr/bin/*", "/usr/sbin/*" "/lib/*", "/lib64/*", "/libx64/*", "/lib32/*", "/libx32/*", "/lib/modules/*", "/lib64/modules/*", "/libx64/modules/*", "/lib32/modules/*", "/libx32/modules/*", "/etc/*", "/boot/*", "/boot/efi/*", "/efi/*",  "/proc/*", "/proc/sys/*", "/sys/*", "/run/*", "/var/*", "/root/*", "/home/*", "/opt/*", "/srv/*", "/usr/local/*", "/user/local/*", "/tmp/*", "/media/*", "/mnt/*"]
fuck_words = ["/"]
# 处理
# 依旧糟糕
match first_words:
# rm系列命令检查附加条件
# 这里有点问题，但暂时没有好的方案，以后会修正
    case "rm":
            if "--" in second_words:
                this_word = int(testnumber+2)
                fileaddress()
                fuck_fileaddress()
            else:
                if "/" in third_words:
                    this_word = int(testnumber+2)
                    fileaddress()
                    fuck_fileaddress()
                elif "-" in third_words:
                    this_word = int(testnumber+3)
                    fileaddress()
                    fuck_fileaddress()
                else:
                    print("E:检查格式是否正确")
# 暂时还不想弄
#    case "rmdir":
#        fileaddress()
#    case "unlink":
#        fileaddress()
    case _:
        print("无效输入")
