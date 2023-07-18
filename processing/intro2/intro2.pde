color fillCol;

void setup() {
  size(800, 800); //cannot use variables as size params
  fillCol = color(255,255,255);
  background(0);
  smooth();
}

void draw() {
  fill(fillCol);
  ellipse(mouseX, mouseY, 10, 10);
}

void keyPressed() {
  if(key=='1') {
    fillCol = color(0,255,0);
  }
  
  if(key=='2') {
    fillCol = color(255, 0, 0);
  }
}
