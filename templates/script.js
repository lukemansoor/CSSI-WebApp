function hasGetUserMedia() {
        return !!(navigator.mediaDevices &&
                navigator.mediaDevices.getUserMedia);
}

if (hasGetUserMedia()) {
        //we gucci
} else {
        alert('getUserMedia() is not supported by your browser');
}
