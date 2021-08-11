#include <Eigen/Dense>
#include <map>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace Eigen;
using namespace std;

int main(int argc, char** argv) {
  int imax = 101;
  MatrixXd P(imax, imax);
  MatrixXd p_star(imax, imax);
  MatrixXd Q(imax-1, imax-1);
  MatrixXd N(imax-1, imax-1);
  MatrixXd eye = MatrixXd::Identity(imax-1, imax-1);
  VectorXd ones(imax-1);
  VectorXd res(imax);

  double expected_moves = 0.0;
  double constraint = 0.0;
  int num_cl = 0, val;
  std::map<int, int> cl;
  std::string line;
  std::ifstream in(argv[1]);
  getline(in, line);
  std::stringstream ss;
  ss << line;
  ss >> num_cl;
  num_cl /= 2;
  int *start, *end;
  start = new int[num_cl];
  end = new int[num_cl];
  for(int n=0;n<num_cl;n++) {
    std::stringstream ss1, ss2;
    getline(in, line);
    ss1 << line;
    ss1 >> val;
    start[n] = val;
    getline(in, line);
    ss2 << line;
    ss2 >> cl[val];
    end[n] = cl[val];
  }

  int extra;
  for(int i=0;i<imax;i++) {
    if(i < (imax-6)) {
      for(int j=i+1;j<i+7;j++) {
        P(i,j) = 1.0/6.0;
      }
    } else {
      extra = (i+6)-imax;
      for(int j=i;j<imax;j++) {
        if(i == j) {
	  P(i,j) = (1.0+extra)/6.0;
	} else {
	  P(i,j) = 1.0/6.0;
	}
      }
    }
  }

  for(int i=0;i<num_cl;i++) {
    if(start[i] == end[i]) {
      constraint = 1.0;
    }
  }
  for(int i=0;i<num_cl;i++) {
    for(int j=0;j<num_cl;j++) {
      if(i != j) {
        if(start[i] == start[j]) {
          constraint = 1.0;
      }
        if(end[i] == end[j]) {
          constraint = 1.0;
        }
      }
    }
  }

  p_star = P;
  if(constraint < 1.0) {
    std::map<int, int>::iterator it;
    for(it = cl.begin(); it != cl.end(); it++) {
      //T(it->first, it->second) = 1.0;
      for(int k=0;k<imax;k++) {
	p_star(it->first,k) = 0.0;
      }
      for(int k=0;k<imax;k++) {
	if(k != it->first) {
	  p_star(k,it->second) = P(k,it->second) +
		  P(k,it->first);
	}
      }
      for(int k=0;k<imax;k++) {
	p_star(k,it->first) = 0.0;
      }
    }

    for(int i=0;i<imax-1;i++) {
      ones(i) = 1.0;
      for(int j=0;j<imax-1;j++) {
	Q(i,j) = p_star(i,j);
      }
    }

    N = eye - Q;
    N = N.inverse();
    res = N * ones;
    expected_moves = res(0);
  
  }

  printf("%30.20f\n",expected_moves);
  double goal = 66.978705007555420778;
  FILE *f;
  f = fopen(argv[2],"w");
  fprintf(f,"%30.20e\n",fabs(expected_moves-goal));
  //fprintf(f,"%30.20e\n",constraint);
  fclose(f);

  return 0;
}
