color fillCol;
void setup() {
  size(800,800);
  smooth();
}

void draw(){
  if(mouseX > width/2) {
    fillCol = color(255, 0, 0);
  }
  else {
    fillCol = color(0,0,255);
  }
  
  fill(fillCol);
  ellipse(mouseX, mouseY, 10, 10);
}
