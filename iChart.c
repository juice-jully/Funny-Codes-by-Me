#include <stdio.h>

int pont1(int a){
    int total;
    if(a == 1){
        total = 10;
    }
    else if(a == 2){
        total = 7;
    }
    else if(a == 3){
        total = 5;
    }
    else if(a >= 4 && a <= 10){
        total = 3;
    }
    else if(a >= 11 && a <= 15){
        total = 2;
    }
    else if(a >= 16 && a <= 20){
        total = 1;
    }
    else if(a>20){
        total = 0;
    }
    return total;
}
int pont2(int b){
    int total;
    if(b == 1){
        total = 10;
    }
    else if(b == 2){
        total = 7;
    }
    else if(b == 3){
        total = 5;
    }
    else if(b == 4 || b == 5){
        total = 3;
    }
    else if(b >= 6 && b <= 10){
        total = 2;
    }
    else if(b >= 11 && b <= 20){
        total = 1;
    }
    else if(b>20){
        total = 0;
    }
    return total;
}

int main (){
  int md, mrt, gd, grt, bd, brt, v, f, y, n, patual;
  float t,pfutura;
  scanf("%d %d %d %d %d %d %d %d %d %d",&md,&mrt,&gd,&grt,&bd,&brt,&v,&f,&y,&n);
  float a=((md+gd+bd+v+f+y)/6.00);
  float b=((mrt+grt+brt)/3.00);
  t=a/b;
  int N=1;
  for(int a=1;a<=n;a++){
      N=N*a;
  }
  
  
  md=pont1(md)*6;
  gd=pont1(gd)*4;
  bd=pont1(bd);
  v=pont1(v)*2;
  f=pont1(f)*3;
  y=pont1(y)*3;
  mrt=pont2(mrt);
  grt=pont2(grt);
  brt=pont2(brt);
  patual = (md+gd+bd+v+f+y+mrt+grt+brt);
  
  
  pfutura = patual -(t * N);
  printf("Pontuação Total:  %d pontos.\nPrevisão em %d dias é de %.0f pontos.",patual,n,pfutura);
  
  
  return 0;

}
