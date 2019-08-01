<template>
  <div class="container">
    <Navigator defaultActive="courseplan"></Navigator>
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
            <span>
              <span style="color:gray; display:inline-block;margin-left: 30px;width:150px;">当前总课时数:</span>
              <span
                style="font-weight: bold; display:inline-block;width:50px;"
                :id="'totalcount' + index"
              ></span>
            </span>
            <span style="float:right;text-align:right;">
              <span style="display: inline-block;margin-right: 30px;" class="cardoperation3" @click="foldallcard">折叠所有</span>
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
            <el-row :gutter="20" style="margin:10px;">
              <el-col :span="6">
                <el-select v-model="tempcourselist[index]" filterable placeholder="请选择课程">
                  <el-option
                    v-for="item in courselist"
                    :key="item.course_id"
                    :label="item.course_name"
                    :value="item.course_id"
                  ></el-option>
                </el-select>
              </el-col>
              <el-col :span="6">
                <el-select v-model="tempteacherlist[index]" filterable placeholder="请选择任课老师">
                  <el-option
                    v-for="item in teacherlist"
                    :key="item.teacher_id"
                    :label="item.teacher_name"
                    :value="item.teacher_id"
                  ></el-option>
                </el-select>
              </el-col>
              <el-col :span="6">
                <el-input v-model="tempcountlist[index]" placeholder>
                  <template slot="prepend">课时数</template>
                </el-input>
              </el-col>
              <el-col :span="6">
                <el-button type="primary" class="mybutton" @click="handleAdd(index)">添加</el-button>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="24">
                <el-table :data="tempcourseplanlist[index]" style="width: 100%">
                  <el-table-column label="课程名称">
                    <template slot-scope="scope">{{scope.row.course_name}}</template>
                  </el-table-column>
                  <el-table-column label="任课教师">
                    <template slot-scope="scope">{{scope.row.teacher_name}}</template>
                  </el-table-column>
                  <el-table-column label="课时数">
                    <template slot-scope="scope">{{scope.row.courseplan_count}}</template>
                  </el-table-column>
                  <el-table-column label="操作">
                    <template slot-scope="scope">
                      <el-button
                        type="info"
                        class="mybutton"
                        @click="handleUpdate(scope.$index, scope.row)"
                      >编辑</el-button>
                      <el-button
                        type="danger"
                        class="mybutton"
                        @click="handleDelete(scope.$index, scope.row)"
                      >删除</el-button>
                    </template>
                  </el-table-column>
                </el-table>
              </el-col>
            </el-row>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Navigator from "@/components/Navigator";
export default {
  name: "courseplan",
  components: {
    Navigator
  },
  data() {
    return {
      classlist: [],
      courselist: [],
      tempcourselist: [],
      teacherlist: [],
      tempteacherlist: [],
      tempcountlist: [],
      tempcourseplanlist: [],
      courseplanlist: []
    };
  },
  created() {
    this.getClassList();
    this.getCourseList();
    this.getTeacherList();
    this.getData();
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
      document.getElementById("content" + index).style = "display:inline-block;";
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
    getData() {
      this.courseplanlist = [];
      this.tempcourseplanlist = [];
      this.axios.get("/courseplan/details/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.courseplanlist = resp["inforesult"];
          for (var m in this.classlist) {
            var templist = [];
            var tempcount = 0;
            for (var n in this.courseplanlist) {
              if (
                this.courseplanlist[n]["class_id"] ==
                this.classlist[m]["class_id"]
              ) {
                templist.push(this.courseplanlist[n]);
                tempcount =
                  tempcount + this.courseplanlist[n]["courseplan_count"];
              }
            }
            document.getElementById("totalcount" + m).innerHTML = tempcount;
            this.tempcourseplanlist.push(templist);
          }
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
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
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    getCourseList() {
      this.axios.get("/course/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.courselist = resp["inforesult"];
          this.courselist.sort((a, b) => {
            return b["course_id"] - a["course_id"];
          });
          for (var i = 0; i < this.classlist.length; i++) {
            this.tempcourselist.push("");
          }
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleAdd(index) {
      this.axios
        .post("/courseplan/", {
          class_id: this.classlist[index].class_id,
          course_id: this.tempcourselist[index],
          teacher_id: this.tempteacherlist[index],
          courseplan_count: this.tempcountlist[index]
        })
        .then(response => {
          var resp = response.data;
          if (resp["infostatus"]) {
            this.getData();
            this.tempcourselist[index] = "";
            this.tempteacherlist[index] = "";
            this.tempcountlist[index] = "";
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
.cla_title {
  text-align: left;
}
.cardoperation1 {
  color: hotpink;
}
.cardoperation1:hover {
  cursor: pointer;
  font-weight: bold;
}
.cardoperation2 {
  color: blueviolet;
}
.cardoperation2:hover {
  cursor: pointer;
  font-weight: bold;
}
.cardoperation3 {
  color: black;
}
.cardoperation3:hover {
  cursor: pointer;
  font-weight: bold;
}
.container{
    margin-top: 100px;
}
</style>
