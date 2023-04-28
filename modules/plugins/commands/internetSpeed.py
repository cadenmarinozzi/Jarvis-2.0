import speedtest

speedTest = speedtest.Speedtest();

def getDownloadSpeed():
    downloadSpeed = speedTest.download();
    formattedDownloadSpeed = str(int(downloadSpeed * 9.537 * 10 ** -7));

    return formattedDownloadSpeed + " megabytes per second";

def getUploadSpeed():
    uploadSpeed = speedTest.upload();
    formattedUploadSpeed = str(int(uploadSpeed * 9.537 * 10 ** -7));

    return formattedUploadSpeed + " megabytes per second";