var Certifico = (function() {
    var inputLogo = $('#certificate-logo'),
        inputLogoValue = $('#certificate-logo-value'),
        inputMessage = $('#certificate-message'),
        previewButton = $('#preview-button'),
        previewCanvas = $('#preview-canvas'),
        previewModal = $('#preview-modal');

    var preview = function() {
        inputLogo.on('change', onInputLogoChange);
        previewButton.on('click', onPreviewButtonClick);
    };

    var print = function(eventLogo, eventMessage) {
        var doc = createPDF(eventLogo, eventMessage);
        window.location = doc.output('datauristring');
    };

    var onInputLogoChange = function(event) {
        var file = inputLogo.get(0).files[0];

        if (file) {
            var reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = function(e) {
                inputLogoValue.val(e.target.result);
            };
        }
    };

    var onPreviewButtonClick = function(event) {
        var doc = createPDF(inputLogoValue.val(), inputMessage.val());

        previewCanvas.attr('src', doc.output('datauristring'));
        previewModal.modal();
    };

    var createPDF = function(eventLogo, eventMessage) {
        var doc = new jsPDF({orientation: 'landscape'}),
            splitedText = doc.splitTextToSize(eventMessage, 225);

        doc.setTextColor(34, 34, 34);
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(34);
        doc.text('CERTIFICADO DE PARTICIPAÇÃO', 50, 80);

        doc.setFont('helvetica', 'normal');
        doc.setFontSize(18);
        doc.text(splitedText, 20, 95);

        if (eventLogo) {
            doc.addImage(eventLogo, 'PNG', 20, 10);
        }

        // theme logo
        doc.addImage(pythonBrasilLogo, 'PNG', 210, 15);

        // signature
        doc.addImage(signature, 'PNG', 105, 150);
        doc.line(200, 160, 100, 160); // horizontal line
        doc.setFontSize(14);
        doc.text('Francisco Helton Alves Chaves', 115, 168);
        doc.text('Organizador da Python Nordeste 2017', 108, 175);

        return doc;
    };

    return {preview: preview, print: print}
})();
