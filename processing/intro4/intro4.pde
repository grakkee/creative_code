int lastMouseX = 0;
int lastMouseY = 0;

void setup() {
  size(600,600);
  ellipseMode(CORNERS);
}

void draw(){}

void mousePressed() {
  if(lastMouseX != 0 && lastMouseY != 0) {
    stroke(random(255), random(255), random(255));
    strokeWeight(random(10));
    fill(random(255), random(255), random(255));
    ellipse(mouseX, mouseY, lastMouseX, lastMouseY);
    lastMouseX = 0;
    lastMouseY = 0;
  }
  
  else {
    lastMouseX = mouseX;
    lastMouseY = mouseY;
  }
}
