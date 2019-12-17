import DarkSkyApi from 'dark-sky-api'

DarkSkyApi.apiKey = '876d0e079a74f725c077238a12dd89f0';
DarkSkyApi.proxy = true;

DarkSkyApi.units = 'si'; // default 'us'
DarkSkyApi.language = 'en'; // default 'en'
DarkSkyApi.postProcessor = (item) => { // default null;
  item.day = item.dateTime.format('ddd');
  return item;
}
DarkSkyApi.loadCurrent()
  .then(result => console.log(result));