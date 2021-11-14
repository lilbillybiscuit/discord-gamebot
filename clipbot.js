const ffmpeg = require('ffmpeg');

try {
  var process = new ffmpeg('path/to/pcm/file');
  process.then(function (audio) {
    audio.fnExtractSoundToMP3('path/to/new/file.mp3', function (error, file) {
      if (!error) console.log('Audio File: ' + file);
    });
  }, function (err) {
    console.log('Error: ' + err);      
  });
} catch (e) {
  console.log(e);
}