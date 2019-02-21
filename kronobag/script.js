$(document).ready(function($) {
    $(".linked-row").click(function() {
        window.open($(this).data('target'), '_blank');
    });
});
