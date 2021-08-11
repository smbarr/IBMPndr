#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <fstream>
#include <glpk.h>

using namespace std;

int main(int argc, char** argv) {
  string line, name;
  int nplayers, id;

  glp_prob *mip = glp_create_prob();
  glp_set_prob_name(mip, "poison");
  glp_set_obj_dir(mip, GLP_MAX);

  int cnt = 1;
  int n_plants = 4;
  int n_days = 2;
  int n_mixtures = 2;
  int n_barrels = 8;
  string *barrel_names;
  barrel_names = new string[n_barrels];
  barrel_names[0] = "A";
  barrel_names[1] = "B";
  barrel_names[2] = "C";
  barrel_names[3] = "D";
  barrel_names[4] = "E";
  barrel_names[5] = "F";
  barrel_names[6] = "G";
  barrel_names[7] = "H";

  int n_dv = n_plants*n_days*n_mixtures*n_barrels+(n_barrels*(n_barrels-1)*n_plants*n_days*n_barrels);
  cout << n_dv << endl;

  int n_constraints = n_barrels*n_barrels*(n_barrels-1);

  glp_add_rows(mip, n_constraints);
  for(int i=0;i<n_barrels;i++) {
    for(int j=0;j<n_barrels;j++) {
      if(i != j) {
        for(int k=0;k<n_barrels;k++) {
          name = barrel_names[i]+"_"+barrel_names[j]+"_const-"+barrel_names[k];
          if(k == i || k == j) {
            glp_set_row_name(mip, cnt, name.c_str());
            glp_set_row_bnds(mip, cnt, GLP_FX, -1.0, 0);
          } else {
            glp_set_row_name(mip, cnt, name.c_str());
            glp_set_row_bnds(mip, cnt, GLP_FX, 0.0, 0);
          }
          cnt++;
        }
      }
    }
  }

  //cnt = 1;
  //for(int n=7+nwr_stacking+nte_stacking+nfixed+1;n<=7+nwr_stacking+nte_stacking+nfixed+n_no_opposing;n++) {
  //  string const_name = "opposing_team_const_"+std::to_string(cnt);
  //  glp_set_row_name(mip, n, const_name.c_str());
  //  glp_set_row_bnds(mip, n, GLP_DB, 0.0, 7.0);
  //  cnt++;
  //}

  glp_add_cols(mip, n_dv);
  cnt = 1;
  for(int p=1;p<=n_plants;p++) {
    for(int d=1;d<=n_days;d++) {
      for(int m=1;m<=n_mixtures;m++) {
        for(int b=1;b<=n_barrels;b++) {
          name = "p"+std::to_string(p)+
                 "d"+std::to_string(d)+
                 "m"+std::to_string(m)+
                 "_"+barrel_names[b-1];
          glp_set_col_name(mip, cnt, name.c_str());
          glp_set_col_bnds(mip, cnt, GLP_DB, 0.0, 1.0);
          glp_set_col_kind(mip, cnt, GLP_IV);
          cnt++;
        }
      }
    }
  }
  for(int i=0;i<n_barrels;i++) {
    for(int j=0;j<n_barrels;j++) {
      if(i != j) {
        for(int p=1;p<=n_plants;p++) {
          for(int d=1;d<=n_days;d++) {
            for(int b=0;b<n_barrels;b++) {
              name = barrel_names[i]+barrel_names[j]+"_"+
                     "p"+std::to_string(p)+
                     "d"+std::to_string(d)+"-"+barrel_names[b];
              glp_set_col_name(mip, cnt, name.c_str());
              glp_set_col_bnds(mip, cnt, GLP_DB, 0.0, 1.0);
              glp_set_col_kind(mip, cnt, GLP_IV);
              cnt++;
            }
          }
        }
      }
    }
  }

  int *ia, *ja;
  double *ar;
  ia = new int[n_dv*n_constraints+1];
  ja = new int[n_dv*n_constraints+1];
  ar = new double[n_dv*n_constraints+1];
  cnt = 1;
  int n = 1;

  for(int i=0;i<n_barrels;i++) {
    for(int j=0;j<n_barrels;j++) {
      if(i != j) {
        for(int k=0;k<n_barrels;k++) {
          for(int p=0;p<n_plants;p++) {
            for(int d=0;d<n_days;d++) {
              for(int m=0;m<n_mixtures;m++) {
                for(int b=0;b<n_barrels;b++) {
                  if(b == k) {
                    ia[cnt] = 1;
                    ja[cnt] = n;
                    ar[cnt] = 0.5;
                    n++;
                    cnt++;
                  } else {
                    ia[cnt] = 1;
                    ja[cnt] = n;
                    ar[cnt] = 0.0;
                    n++;
                    cnt++;
                  }
                }
              }
            }
          }
          for(int i2=0;i2<n_barrels;i2++) {
            for(int j2=0;j2<n_barrels;j2++) {
              if(i2 != j2) {
                for(int p=0;p<n_plants;p++) {
                  for(int d=0;d<n_days;d++) {
                    for(int b=0;b<n_barrels;b++) {
                      if(b == k) {
                        ia[cnt] = 1;
                        ja[cnt] = n;
                        ar[cnt] = 1.0;
                        n++;
                        cnt++;
                      } else {
                        ia[cnt] = 1;
                        ja[cnt] = n;
                        ar[cnt] = 0.0;
                        n++;
                        cnt++;
                      }
                    }
                  }
                }
              }
            }
          }
          n++;
        }
      }
    }
  }
/*

  while(dit != salary.end()) {
    ia[cnt] = 1;
    ja[cnt] = n+1;
    ar[cnt] = salary[dit->first];
    n++;
    cnt++;
    dit++;
  }
  iit = pos_id.begin();
  n = 0;
  while(iit != pos_id.end()) {
    ia[cnt] = 2;
    ja[cnt] = n+1;
    if(pos_id[iit->first] == 1) {
      ar[cnt] = 1.0;
    } else {
      ar[cnt] = 0.0;
    }
    n++;
    cnt++;
    iit++;
  }

  iit = pos_id.begin();
  n = 0;
  while(iit != pos_id.end()) {
    ia[cnt] = 3;
    ja[cnt] = n+1;
    if(pos_id[iit->first] == 2) {
      ar[cnt] = 1.0;
    } else {
      ar[cnt] = 0.0;
    }
    n++;
    cnt++;
    iit++;
  }
  iit = pos_id.begin();
  n = 0;
  while(iit != pos_id.end()) {
    ia[cnt] = 4;
    ja[cnt] = n+1;
    if(pos_id[iit->first] == 3) {
      ar[cnt] = 1.0;
    } else {
      ar[cnt] = 0.0;
    }
    n++;
    cnt++;
    iit++;
  }
  iit = pos_id.begin();
  n = 0;
  while(iit != pos_id.end()) {
    ia[cnt] = 5;
    ja[cnt] = n+1;
    if(pos_id[iit->first] == 4) {
      ar[cnt] = 1.0;
    } else {
      ar[cnt] = 0.0;
    }
    n++;
    cnt++;
    iit++;
  }
  iit = pos_id.begin();
  n = 0;
  while(iit != pos_id.end()) {
    ia[cnt] = 6;
    ja[cnt] = n+1;
    if(pos_id[iit->first] == 5) {
      ar[cnt] = 1.0;
    } else {
      ar[cnt] = 0.0;
    }
    n++;
    cnt++;
    iit++;
  }
  iit = pos_id.begin();
  n = 0;
  while(iit != pos_id.end()) {
    ia[cnt] = 7;
    ja[cnt] = n+1;
    if(pos_id[iit->first] == 2 ||
       pos_id[iit->first] == 3 ||
       pos_id[iit->first] == 4) {
      ar[cnt] = 1.0;
    } else {
      ar[cnt] = 0.0;
    }
    n++;
    cnt++;
    iit++;
  }

  if(stack_wr) {
    // WR Stacking
    sit = team.begin();
    for(int t=1;t<=nteams;t++) {
      iit = pos_id.begin();
      n = 0;
      while(iit != pos_id.end()) {
        ia[cnt] = 7+t;
        ja[cnt] = n+1;
        if((teams_playing[t] == team[iit->first]) && (pos_id[iit->first] == 1)) {
          // The negative number determines how many players get stacked.
          //   ie: 1 = one receiver on same team as QB,
          //       2 = two receivers on same team as QB
          ar[cnt] = -1.0;
          //ar[cnt] = -2.0;
        } else if((teams_playing[t] == team[iit->first]) && (pos_id[iit->first] == 3)) {
          ar[cnt] = 1.0;
        } else {
          ar[cnt] = 0.0;
        }
        n++;
        cnt++;
        iit++;
      }
      sit++;
    }
  }

  if(fixes) {
    // Fixed Constraints
    iit = pos_id.begin();
    n = 0;
    while(iit != pos_id.end()) {
      ia[cnt] = 7+nwr_stacking+nte_stacking+1;
      ja[cnt] = n+1;
      if(pos_id[iit->first] == 5 and team[iit->first] == "NOS") {
        ar[cnt] = 1.0;
      } else {
        ar[cnt] = 0.0;
      }
      n++;
      cnt++;
      iit++;
    }
  }

  // Non-opposing Constraints
  sit = team.begin();
  for(int t=1;t<=nteams;t++) {
    iit = pos_id.begin();
    n = 0;
    while(iit != pos_id.end()) {
      ia[cnt] = 7+nwr_stacking+nte_stacking+nfixed+t;
      ja[cnt] = n+1;
      if((teams_playing[t] == games[team[iit->first]]) && (pos_id[iit->first] != 5)) {
        ar[cnt] = 1.0;
      } else if((teams_playing[t] == team[iit->first]) && (pos_id[iit->first] == 5)) {
        ar[cnt] = 7.0;
      } else {
        ar[cnt] = 0.0;
      }
      n++;
      cnt++;
      iit++;
    }
    sit++;
  }

  glp_load_matrix(mip, nplayers*(7+nwr_stacking+nte_stacking+nfixed+n_no_opposing), ia, ja, ar);

  glp_iocp parm;
  glp_init_iocp(&parm);
  glp_cpxcp cpparm;
  glp_init_cpxcp(&cpparm);
  parm.presolve = GLP_ON;
  int err = glp_intopt(mip, &parm);

  glp_write_lp(mip, &cpparm, "out.lp");

  printf("\n\nQBS:\n");
  cnt = 1;
  iit = pos_id.begin();
  while(iit != pos_id.end()) {
    if (pos_id[iit->first] == 1 && glp_mip_col_val(mip, cnt) == 1) {
      printf(" - %s : %5.1f\n",iit->first.c_str(), salary[iit->first]);
    }
    cnt++;
    iit++;
  }

  glp_delete_prob(mip);
*/
  return 0;
}
