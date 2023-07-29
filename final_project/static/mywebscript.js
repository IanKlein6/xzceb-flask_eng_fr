let translateToFrench = () => {
    let textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            document.getElementById("translated_text").innerHTML = response.translated_text;
        }
    };
    xhttp.open("GET", "/englishToFrench?textToTranslate=" + encodeURIComponent(textToTranslate), true);
    xhttp.send();
};

let translateToEnglish = () => {
    let textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            document.getElementById("translated_text").innerHTML = response.translated_text;
        }
    };
    xhttp.open("GET", "/frenchToEnglish?textToTranslate=" + encodeURIComponent(textToTranslate), true);
    xhttp.send();
};
