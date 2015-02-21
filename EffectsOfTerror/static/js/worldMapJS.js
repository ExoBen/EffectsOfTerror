function handleMapClick(e, code) {
    var map = $('#world-map').vectorMap('get', 'mapObject');
    window.location.href = "/search/?query=" + map.getRegionName(code);
    return;
}
