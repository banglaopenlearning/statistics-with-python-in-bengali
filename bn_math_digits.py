import re, sys

bn = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    # কোড ব্লক আলাদা রেখে শুধু বাকি লেখার ভেতরের সূত্র বদলানো
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"\$\$.*?\$\$|\$[^$\n]+\$",
                          lambda m: m.group(0).translate(bn), parts[i], flags=re.S)
    open(path, "w", encoding="utf-8").write("".join(parts))
    print(path, "done")