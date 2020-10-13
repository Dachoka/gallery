function copyFunction(){
    var copyLink = document.getElementById("imgLink");

    copyLink.select();
    copyLink.setSelectionRange(0, 99999)

    document.execCommand("copy");

    alert("Copied to clipboard!")
}