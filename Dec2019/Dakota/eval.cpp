#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

double calc_mse(double *x);
double func(double *x, double xa);

int main(int argc, char** argv) {
  ifstream params(argv[1]);
  string line;

  double *vars;
  vars = new double[4];

  getline(params, line);
  for(int i=0;i<4;i++) {
    getline(params, line);
    stringstream ss;
    ss << line;
    ss >> vars[i];
  }

  double mse = calc_mse(vars);
  FILE *f;
  f = fopen(argv[2],"w");
  fprintf(f,"%e\n",mse);
  fclose(f);
 
  return 0;
}

double calc_mse(double *x) {
  double mse;
  double nmax = 1001;
  double dn = 2.0/(nmax-1);
  double xa;
  for(int n=0;n<nmax;n++) {
    xa = static_cast<double>(n)*dn-1.0;
    mse += pow(func(x, xa)-abs(xa),2);
  }
  mse = mse / nmax;

  return mse;
}

double func(double *x, double xa) {
  double res;
  res = x[0]/pow(xa,4)+x[1]/pow(xa,2)+x[2]*pow(xa,2)+x[3]*pow(xa,4);
  return res;
}
