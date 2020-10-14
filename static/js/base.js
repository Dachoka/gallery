document.querySelector("#linkButton").addEventListener("click",copyFunction);

function copyFunction(){
    var copyLink = document.querySelector("#imgLink");

    copyLink.select();
    copyLink.setSelectionRange(0, 99999)

    document.execCommand("copy");

    alert("Copied to clipboard!")
}