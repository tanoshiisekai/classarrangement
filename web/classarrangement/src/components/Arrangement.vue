<template>
  <div class="container">
    <Navigator defaultActive="arrangement"></Navigator>
    <el-row v-for="(cla, index) in classlist" :key="cla.class_id" style="margin:20px;">
      <el-col :span="20" :offset="2">
        <el-card class="box-card" shadow="always">
          <div slot="header" class="cla_title">
            <span style="display:inline-block;width:300px;">
              <span style="font-weight: bold;">{{cla.class_name}}</span>
            </span>
            <span>
              <span style="color:gray; display:inline-block;width:80px;">班主任:</span>
              <span
                style="font-weight: bold; display:inline-block;width:220px;"
              >{{cla.teacher_name}}</span>
            </span>
            <span style="float:right;text-align:right;">
              <span
                style="display: inline-block;margin-right: 30px;"
                class="cardoperation3"
                @click="foldallcard"
              >折叠所有</span>
              <span
                style="margin-right: 30px;"
                class="cardoperation1"
                @click="foldcard(index)"
                :id="'foldcard'+index"
              >折叠卡片</span>
              <span
                style="margin-right: 30px;display: none;"
                class="cardoperation2"
                @click="showcard(index)"
                :id="'showcard'+index"
              >打开卡片</span>
            </span>
          </div>
          <div class="cla_content" :id="'content'+index">
            <div class="datatable" style="float: left;width: 665px;">
              <vxe-table :data.sync="tableData">
                <vxe-table-column type="index" width="30"></vxe-table-column>
                <vxe-table-column field="monday" title="一" width="90"></vxe-table-column>
                <vxe-table-column field="tuesday" title="二" width="90"></vxe-table-column>
                <vxe-table-column field="wedensday" title="三" width="90"></vxe-table-column>
                <vxe-table-column field="thirsday" title="四" width="90"></vxe-table-column>
                <vxe-table-column field="friday" title="五" width="90"></vxe-table-column>
                <vxe-table-column field="saturday" title="六" width="90"></vxe-table-column>
                <vxe-table-column field="sunday" title="日" width="90"></vxe-table-column>
              </vxe-table>
            </div>
            <div class="operationpad" style="float: left;width: 530px;text-align:left;">
              <el-tag
                class="mylabel"
                style="margin-left: 30px;margin-top: 20px;margin-bottom:20px;width:450px;"
              >待排课程</el-tag>
              <div :id="'unarranged'+index" class="mytextbox"></div>
              <el-tag
                class="mylabel"
                style="margin-left: 30px;margin-top: 20px;margin-bottom:20px;width:450px;"
              >排课</el-tag>
              <el-select
                v-model="tempcourselist[index]"
                filterable
                placeholder="请选择课程"
                style="margin-left: 50px;width:400px;"
              >
                <el-option
                  v-for="item in courselist[index]"
                  :key="item.course_id"
                  :label="item.course_name"
                  :value="item.course_id"
                ></el-option>
              </el-select>
              <el-input
                v-model="coursetime[index]"
                placeholder
                style="margin-left: 50px;margin-top: 20px;margin-bottom: 20px;width: 400px;"
              >
                <template slot="prepend">上课时间</template>
              </el-input>
              <el-select
                v-model="tempclassroomlist[index]"
                filterable
                placeholder="请选择教室"
                style="margin-left: 50px;width:400px;"
              >
                <el-option
                  v-for="item in classroomlist"
                  :key="item.classroom_id"
                  :label="item.classroom_name"
                  :value="item.classroom_id"
                ></el-option>
              </el-select>
              <el-checkbox
                v-model="ignoreclassroomlist[index]"
                style="float: left;margin-left: 50px;margin-top: 20px; width:400px;"
              >忽略教室冲突</el-checkbox>
              <el-checkbox
                v-model="ignoreteacherlist[index]"
                style="float: left;margin-left: 50px;margin-top: 20px; width:400px;"
              >忽略任课教师冲突</el-checkbox>
              <el-checkbox
                v-model="ignorecoursetimelist[index]"
                style="float: left;margin-left: 50px;margin-top: 20px; width:400px;"
              >忽略上课时间冲突</el-checkbox>
              <el-button
                type="primary"
                class="mybutton"
                @click="handleAdd(index)"
                style="margin-left: 300px;margin-top: 20px;margin-bottom: 20px;width: 150px;"
              >排入课表</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Navigator from "@/components/Navigator";
export default {
  name: "arrangement",
  components: {
    Navigator
  },
  data() {
    return {
      classlist: [],
      tempteacherlist: [],
      classroomlist: [],
      tempcourselist: [],
      courselist: [],
      courseplanlist: [],
      courseplanbyclasslist: [],
      tempclassroomlist: [],
      coursetime: [],
      ignoreclassroomlist: [],
      ignoreteacherlist: [],
      ignorecoursetimelist: [],
      tableData: [{ monday: "", tuesday: "" }, { monday: "", tuesday: "" }]
    };
  },
  created() {
    this.getClassList();
    this.getTeacherList();
    this.getCoursePlanList();
    this.getClassroomList();
  },
  methods: {
    foldcard(index) {
      document.getElementById("content" + index).style = "display:none";
      document.getElementById("showcard" + index).style =
        "display:inline-block;;margin-right:30px;";
      document.getElementById("foldcard" + index).style =
        "display:none;margin-right:30px;";
    },
    showcard(index) {
      document.getElementById("content" + index).style =
        "display:inline-block;";
      document.getElementById("foldcard" + index).style =
        "display:inline-block;;margin-right:30px;";
      document.getElementById("showcard" + index).style =
        "display:none;margin-right:30px;";
    },
    foldallcard() {
      for (var i in this.classlist) {
        document.getElementById("content" + i).style = "display:none";
        document.getElementById("showcard" + i).style =
          "display:inline-block;;margin-right:30px;";
        document.getElementById("foldcard" + i).style =
          "display:none;margin-right:30px;";
      }
    },
    getTeacherList() {
      this.axios.get("/teacher/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.teacherlist = resp["inforesult"];
          this.teacherlist.sort((a, b) => {
            return b["teacher_id"] - a["teacher_id"];
          });
          for (var i = 0; i < this.classlist.length; i++) {
            this.tempteacherlist.push("");
          }
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    getClassList() {
      this.axios.get("/class/details/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.classlist = resp["inforesult"];
          this.classlist.sort((a, b) => {
            return b["class_id"] - a["class_id"];
          });
          for (var i = 0; i < this.classlist.length; i++) {
            this.coursetime.push("");
          }
          for (var i = 0; i < this.classlist.length; i++) {
            this.ignoreclassroomlist.push(false);
          }
          for (var i = 0; i < this.classlist.length; i++) {
            this.ignoreteacherlist.push(false);
          }
          for (var i = 0; i < this.classlist.length; i++) {
            this.ignorecoursetimelist.push(false);
          }
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    getCoursePlanList() {
      this.axios.get("/courseplan/details/arrangement/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.courseplanlist = resp["inforesult"];
          console.log(this.courseplanlist);
          for (var m in this.classlist) {
            var templist = [];
            var tempcourselist = [];
            var tempcount = 0;
            var unarranged = "";
            for (var n in this.courseplanlist) {
              if (
                this.courseplanlist[n]["class_id"] ==
                this.classlist[m]["class_id"]
              ) {
                templist.push(this.courseplanlist[n]);
                unarranged =
                  unarranged +
                  '<span class="unarranged">' +
                  this.courseplanlist[n]["course_name"] +
                  "</span>";
                tempcourselist.push({
                  course_id: this.courseplanlist[n]["course_id"],
                  course_name: this.courseplanlist[n]["course_name"]
                });
              }
              document.getElementById("unarranged" + m).innerHTML = unarranged;
            }
            this.courseplanbyclasslist.push(templist);
            this.courselist.push(tempcourselist);
          }
          console.log(this.courseplanbyclasslist);
          console.log(this.courselist);
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    getClassroomList() {
      this.axios.get("/classroom/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.classroomlist = resp["inforesult"];
          this.classroomlist.sort((a, b) => {
            return a["classroom_name"] - b["classroom_name"];
          });
          for (var i = 0; i < this.classlist.length; i++) {
            this.tempclassroomlist.push("");
          }
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleAdd(classindex) {
      var newcourse = this.tempcourselist[classindex];
      var newcoursetime = this.coursetime[classindex];
      var newclassroom = this.tempclassroomlist[classindex];
      var newclass = this.classlist[classindex]["class_id"];
      var ignoreclassroom = this.ignoreclassroomlist[classindex];
      if (ignoreclassroom == false) {
        ignoreclassroom = 0;
      } else {
        ignoreclassroom = 1;
      }
      var ignoreteacher = this.ignoreteacherlist[classindex];
      if (ignoreteacher == false) {
        ignoreteacher = 0;
      } else {
        ignoreteacher = 1;
      }
      var ignorecoursetime = this.ignorecoursetimelist[classindex];
      if (ignorecoursetime == false) {
        ignorecoursetime = 0;
      } else {
        ignorecoursetime = 1;
      }
      //console.log(ignoreclassroom);
      //console.log(ignoreteacher);
      //console.log(ignorecoursetime);
      // console.log(newclass);
      // console.log(newcourse);
      // console.log(newcoursetime);
      // console.log(newclassroom);
      this.axios
        .post("/arrangement/", {
          class_id: newclass,
          course_id: newcourse,
          classroom_id: newclassroom,
          coursetime: newcoursetime,
          ignoreclassroom: ignoreclassroom,
          ignoreteacher : ignoreteacher,
          ignorecoursetime: ignorecoursetime
        })
        .then(response => {
          var resp = response.data;
          if (resp["infostatus"]) {
            this.tempcourselist[classindex] = "";
            this.coursetime[classindex] = "";
            this.tempclassroomlist[classindex] = "";
            this.ignoreclassroomlist[classindex] = false;
            this.ignoreteacherlist[classindex] = false;
            this.ignorecoursetimelist[classindex] = false;
          }
          this.$message({
            message: resp["infomsg"]
          });
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
.mytextbox {
  margin-left: 50px;
  font-weight: bold;
}
.unarranged {
  float: left;
  margin-right: 10px;
  height: 25px;
  line-height: 25px;
  margin-bottom: 10px;
  background-color: #eeeeee;
  font-weight: bold;
}
</style>
