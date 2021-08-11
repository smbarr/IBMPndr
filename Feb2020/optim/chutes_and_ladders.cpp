#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <map>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace boost::numeric::ublas;

int main(int argc, char** argv) {
  matrix<double> M(101, 101);
  matrix<double> T(101, 101);
  vector<double> e1(101), res(101);

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
  for(int n=0;n<num_cl;n++) {
    std::stringstream ssi;
    getline(in, line);
    ssi << line;
    ssi >> val;
    ssi >> cl[val];
  }

  for(int i=0;i<101;i++) {
    e1(i) = 0.0;
    for(int j=0;j<101;j++) {
      M(i,j) = 0.0;
      T(i,j) = 0.0;
    }
  }
  e1(0) = 1.0;

  for(int i=1;i<100;i++) {
    int cnt = fmax(0,i-6);
    for(int j=cnt;j<i;j++) {
      M(i,j) = 1.0/6.0;
    }
  }
  for(int i=1;i<7;i++) {
    M(100,100-i) = (7.0-i)/6.0;
  }
  M(100,100) = 1.0;

  int *start, *end;
  start = new int[num_cl];
  end = new int[num_cl];
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
        } else if(end[i] == end[j]) {
          constraint = 1.0;
        }
      }
    }
  }

  if(constraint < 1.0) {
    std::map<int, int>::iterator it;
    for(it = cl.begin(); it != cl.end(); it++) {
      T(it->first, it->second) = 1.0;
    }
  
    for(int j=0;j<101;j++) {
      double sum = 0.0;
      for(int i=0;i<101;i++) {
        sum += T(i,j);
      }
      if(sum == 0.0) {
        T(j,j) = 1.0;
      }
    }
  
    int nmoves = 1000;
    double *win_prob;
    win_prob = new double[nmoves];
    res = e1;
    vector<double> temp(101);
    for(int n=0;n<nmoves;n++) {
      //res = prod(M, res);
      temp = prod(M, res);
      res = prod(T, temp);
      //std::cout << res(100) << std::endl;
      win_prob[n] = res(100);
    }
  
    for(int n=1;n<nmoves;n++) {
      expected_moves += (static_cast<double>(n+1)*(win_prob[n]-win_prob[n-1]));
    }
  }

  double goal = 66.978705007555420778;
  FILE *f;
  f = fopen(argv[2],"w");
  fprintf(f,"%30.20e\n",fabs(expected_moves-goal));
  fprintf(f,"%30.20e\n",constraint);
  fclose(f);

  return 0;
}
