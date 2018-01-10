import urllib.request
import os
import time
import sys
import errno
import calendar


print("** Make sure loaded Url's into the text file **\n")

item_name = input("Enter Url's text file name (Without extension): ").title()
filename = item_name+".txt"



def writeto(rname, rsummary, rtime, rtotal, rfail):
    print('Generating report...')

    label = "<------------------- Report ---------------->\n\n"
    dir = "# Directory name --> " + rname + "\n\n"
    total = "# Total No.of Url's --> " + str(rtotal) + "\n\n"
    failed = "# Failed --> " + str(rfail) + "\n\n"
    time = "# Total time --> " + str(rtime) + "s"

    final_report = label + dir + total + rsummary + failed + time

    fname = rname + "_report.txt"

    try:
            file = open(fname, 'a')
            file.write(final_report)
            file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0)  # quit Python
    print('Done')
    input("\nPress Enter")


with open(filename) as f:
    print("\nDownloading...\n")

    try:
        os.makedirs(item_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    content = f.readlines()
    i = 0

    start = time.time()
    content = [x.strip() for x in content]
    total = len(content)
    for line in content:
        timestamp = calendar.timegm(time.gmtime())
        try:
            urllib.request.urlretrieve(line, os.path.join(item_name, item_name+ str(timestamp) + str(i) + ".jpg"))
            print("Image saved for {0}".format(line))
            i += 1
        except:
            pass

    print("\nDownload Completed")
    end = time.time()
    time = end - start
    summary = "# Total images downloaded --> " + str(i) + "\n\n"  # Failed 5
    fail = (total) - i

writeto(item_name, summary, time, total, fail)
