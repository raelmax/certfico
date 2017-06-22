var CertBrite = (function() {
    var inputLogo = $('#certificate-logo'),
        inputText = $('#certificate-text'),
        previewButton = $('#preview-button'),
        previewCanvas = $('#preview-canvas'),
        previewModal = $('#preview-modal'),
        logoDataURL = null;

    var init = function () {
        setListeners();
    };

    var setListeners = function() {
        inputLogo.on('change', onInputLogoChange);
        previewButton.on('click', onPreviewButtonClick);
    };

    var onInputLogoChange = function(event) {
        var file = inputLogo.get(0).files[0];

        if (file) {
            var reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = function(e) {
                logoDataURL = e.target.result;
            };
        }
    };

    var onPreviewButtonClick = function(event) {
        var doc = createPDF();

        previewCanvas.attr('src', doc.output('datauristring'));
        previewModal.modal();
    };

    var send = function() {};

    var createPDF = function() {
        var doc = new jsPDF({orientation: 'landscape'}),
            splitedText = doc.splitTextToSize(inputText.val().toUpperCase(), 225);

        doc.setTextColor(34, 34, 34);
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(34);
        doc.text('CERTIFICADO DE PARTICIPAÇÃO', 50, 80);

        doc.setFont('helvetica', 'normal');
        doc.setFontSize(18);
        doc.text(splitedText, 20, 95);

        if (logoDataURL) {
            doc.addImage(logoDataURL, 'PNG', 20, 10);
        }

        // theme logo
        doc.addImage(pythonBrasilLogo, 'PNG', 210, 15);

        // signature
        doc.line(200, 160, 100, 160); // horizontal line
        doc.setFontSize(14);
        doc.text('Responsável', 135, 165);

        return doc;
    };

    return {init: init}
})();
