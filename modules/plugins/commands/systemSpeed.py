import psutil, math

def getCPUSpeed():
    usage = psutil.cpu_percent();
    formattedUsage = str(math.floor(usage));

    return formattedUsage;

def getRamSpeed():
    used = psutil.virtual_memory().used;
    i = int(math.floor(math.log(used, 1024)));
    sizeBytes = math.floor(used);
    usage = (sizeBytes == 0 and "0B" or "%s %s" % (round(sizeBytes / math.pow(1024, i), 2), ("Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes")[i]));
    
    return usage;
