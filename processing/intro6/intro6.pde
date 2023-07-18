int posX = 0;
int posY = 300;
int speed = 5;
int targetSize = 200;
boolean movingLeft = false;
boolean movingRight = true;

void setup() {
  size(600,600);
  //background(0);
}

void draw() {
  background(0);
  fill(255,0,0);
  ellipse(300,300,targetSize, targetSize);
  
  if(movingRight) {
    posX = posX + speed;
  }
  
  else if(movingLeft) {
    posX = posX - speed;
  }
  
  if(posX >= width) {
    movingLeft = true;
    movingRight = false;
  }
  
  else if(posX <= 0) {
    movingLeft = false;
    movingRight = true;
  }
  
  fill(0,0,255);
  ellipse(posX,posY,50,50);
}
