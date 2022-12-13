def colorFade(strip, colorFrom, colorTo, wait_ms=20, steps=10):
    steps = 200

    step_R = int(colorTo[0]) / steps
    step_G = int(colorTo[1]) / steps
    step_B = int(colorTo[2]) / steps
    r = int(colorFrom[0])
    g = int(colorFrom[1])
    b = int(colorFrom[2])

    for x in range(steps):
        c = Color(int(r), int(g), int(b))
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, c)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        r += step_R
        g += step_G
        b += step_B