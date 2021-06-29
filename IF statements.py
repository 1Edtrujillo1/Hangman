
# Python ----

def check(x):

    names = ["a", "b", "c"]
    options = ["Option 1", "Option 2", "Option 3"]

    if x in names:
        print({names[i]: options[i] for i in range(len(names))}[x])
    else:
        print("Other option")


check(x="d")


def check_2(x):
    if x == "a":
        print("option 1")
    elif x == "b":
        print("option 2")
    elif x == "c":
        print("option 3")
    else:
        print("other option")


check_2(x="d")

# R ----

library(purrr)


check < - function(x) {
    names < - c("a", "b", "c")
    output < - tryCatch(
        {
            if (x % in % names) {
                output < - list("option 1", "option 2", "option 3") % > %
                set_names("a", "b", "c") % > %
                pluck(x)
            }
            output
        },
        error=function(e) "Other option"
    )
    output
}

check(x="d")


check_2 < - function(x) {
    if (x == "a") {
        print("option 1")
    } else if (x == "b") {
        print("option 2")
    } else if (x == "c") {
        print("option 3")
    } else {
        print("Other option")
    }
}

check_2(x="d")
