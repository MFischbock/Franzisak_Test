var video;

function setup() {
  createCanvas(320, 240);
  pixelDensity(1);
  video = createCapture(VIDEO);
  video.size(320, 240)
}

function draw() {
  
  video.loadPixels();
  loadPixels();
  
  for (var y = 0; y < height; y++) {
    for (var x = 0; x < width; x++) {
      var index = (x + y * width)*4;
      pixels[index+0] = 200;
      pixels[index+1] = video.pixels[index+1];
      pixels[index+2] = video.pixels[index+2];
      pixels[index+3] = 255;
  }
}
  
  updatePixels();
}
