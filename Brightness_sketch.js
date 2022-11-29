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
      var r = video.pixels[index+0];
      var g = video.pixels[index+1];
      var b = video.pixels[index+2];
      
      var bright = (r+g+b)/4;
      var threshold = 255;
      
      if (bright > threshold) {
        fill(255);
      } else {
        fill(0);
      }
      
      pixels[index+0] = r;
      pixels[index+1] = bright;
      pixels[index+2] = bright;
      pixels[index+3] = 254;
    }
  }
  
  updatePixels();
}
