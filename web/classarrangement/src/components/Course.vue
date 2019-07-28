<template>
  <div class="container">
    <Navigator defaultActive="course"></Navigator>
    <el-row :gutter="20" style="margin:10px;">
      <el-col :span="12">
        <el-input v-model="course_name" placeholder id="crname">
          <template slot="prepend">课程名称</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-select v-model="course_isgroup" filterable placeholder="是否合班">
          <el-option key="0" label="否" value="0"></el-option>
          <el-option key="1" label="是" value="1"></el-option>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" class="mybutton" @click="this.handleAdd">添加</el-button>
      </el-col>
    </el-row>
    <el-row style="margin:30px;">
      <el-card class="box-card">
        <el-row style="margin:10px;">
          <el-col :span="8">
            <el-select v-model="class_name_1" filterable placeholder="请选择班级1">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="class_name_2" filterable placeholder="请选择班级2">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="class_name_3" filterable placeholder="请选择班级3">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row style="margin:10px;">
          <el-col :span="8">
            <el-select v-model="class_name_4" filterable placeholder="请选择班级4">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="class_name_5" filterable placeholder="请选择班级5">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="class_name_6" filterable placeholder="请选择班级6">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row style="margin:10px;">
          <el-col :span="8">
            <el-select v-model="class_name_7" filterable placeholder="请选择班级7">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="class_name_8" filterable placeholder="请选择班级8">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="class_name_9" filterable placeholder="请选择班级9">
              <el-option
                v-for="item in classlist"
                :key="item.class_id"
                :label="item.class_name"
                :value="item.class_id"
              ></el-option>
            </el-select>
          </el-col>
        </el-row>
      </el-card>
    </el-row>
    <el-row style="margin:30px;">
      <el-col :span="24">
        <el-table :data="courselist" style="width: 100%">
          <el-table-column label="课程名称">
            <template slot-scope="scope">{{scope.row.course_name}}</template>
          </el-table-column>
          <el-table-column label="是否合班">
            <template slot-scope="scope">
              <span v-if="scope.row.course_isgroup==1">是</span>
              <span v-else>否</span>
            </template>
          </el-table-column>
          <el-table-column label="合班清单">
            <template slot-scope="scope">{{scope.row.course_classlist}}</template>
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
    <el-dialog title="编辑课程信息" :visible.sync="updatedialog">
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">课程名称</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="course_name_new" placeholder class="samelengthwithselect"></el-input>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">是否合班</el-tag>
        </el-col>
        <el-col :span="14">
          <el-select
            v-model="course_isgroup_new"
            filterable
            placeholder="是否合班"
            class="samelengthwithselect"
          >
            <el-option key="0" label="否" value="0"></el-option>
            <el-option key="1" label="是" value="1"></el-option>
          </el-select>
        </el-col>
      </el-row>
      <el-row :gutter="20" style="margin:10px;">
        <el-col :span="8">
          <el-select v-model="class_name_1_new" filterable placeholder="请选择班级1">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-select v-model="class_name_2_new" filterable placeholder="请选择班级2">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-select v-model="class_name_3_new" filterable placeholder="请选择班级3">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
      </el-row>
      <el-row :gutter="20" style="margin:10px;">
        <el-col :span="8">
          <el-select v-model="class_name_4_new" filterable placeholder="请选择班级4">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-select v-model="class_name_5_new" filterable placeholder="请选择班级5">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-select v-model="class_name_6_new" filterable placeholder="请选择班级6">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
      </el-row>
      <el-row :gutter="20" style="margin:10px;">
        <el-col :span="8">
          <el-select v-model="class_name_7_new" filterable placeholder="请选择班级7">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-select v-model="class_name_8_new" filterable placeholder="请选择班级8">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
        <el-col :span="8">
          <el-select v-model="class_name_9_new" filterable placeholder="请选择班级9">
            <el-option
              v-for="item in classlist"
              :key="item.class_id"
              :label="item.class_name"
              :value="item.class_id"
            ></el-option>
          </el-select>
        </el-col>
      </el-row>
      <div slot="footer" class="dialog-footer">
        <el-button @click="updatedialog=false">取消</el-button>
        <el-button type="primary" @click="handleSubUpdate">确定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import Navigator from "@/components/Navigator";
export default {
  name: "course",
  components: {
    Navigator
  },
  data() {
    return {
      course_name: "",
      course_name_new: "",
      course_isgroup: "0",
      course_isgroup_new: "",
      classlist: [],
      courselist: [],
      class_name_1: "",
      class_name_2: "",
      class_name_3: "",
      class_name_4: "",
      class_name_5: "",
      class_name_6: "",
      class_name_7: "",
      class_name_8: "",
      class_name_9: "",
      class_name_1_new: "",
      class_name_2_new: "",
      class_name_3_new: "",
      class_name_4_new: "",
      class_name_5_new: "",
      class_name_6_new: "",
      class_name_7_new: "",
      class_name_8_new: "",
      class_name_9_new: "",
      updatedialog: false,
      courseid_updated: ""
    };
  },
  mounted() {
    document.getElementById("crname").focus();
  },
  created() {
    var lett = this;
    document.onkeydown = function(e) {
      var key = window.event.keyCode;
      if (key == 13) {
        lett.handleAdd();
      }
    };
    this.getClassList();
    this.getData();
  },
  methods: {
    getData() {
      this.axios.get("/course/details/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.courselist = resp["inforesult"];
          this.courselist.sort((a, b) => {
            return b["course_id"] - a["course_id"];
          });
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    getClassList() {
      this.axios.get("/class/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.classlist = resp["inforesult"];
          this.classlist.sort((a, b) => {
            return a["class_name"] > b["class_name"];
          });
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleSubUpdate() {
      var classliststr_new =
        this.class_name_1_new +
        "," +
        this.class_name_2_new +
        "," +
        this.class_name_3_new +
        "," +
        this.class_name_4_new +
        "," +
        this.class_name_5_new +
        "," +
        this.class_name_6_new +
        "," +
        this.class_name_7_new +
        "," +
        this.class_name_8_new +
        "," +
        this.class_name_9_new;
      console.log(classliststr_new);
      this.axios
        .post("/course/update/" + this.courseid_updated, {
          course_name: this.course_name_new,
          course_isgroup: this.course_isgroup_new,
          course_classlist: classliststr_new
        })
        .then(response => {
          var resp = response.data;
          this.$message({
            message: resp["infomsg"]
          });
          this.updatedialog = false;
          this.getData();
          this.course_name_new = "";
          this.course_isgroup_new = "";
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleUpdate(index, row) {
      this.updatedialog = true;
      this.axios.get("/course/" + row.course_id).then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          var redata = resp["inforesult"];
          this.course_name_new = redata["course_name"];
          this.course_isgroup_new = redata["course_isgroup"].toString();
          this.course_classlist = redata["course_classlist"];
          var clist = this.course_classlist.split(",");
          if (clist[0]) {
            this.class_name_1_new = parseInt(clist[0]);
          } else {
            this.class_name_1_new = "";
          }
          if (clist[1]) {
            this.class_name_2_new = parseInt(clist[1]);
          } else {
            this.class_name_2_new = "";
          }
          if (clist[2]) {
            this.class_name_3_new = parseInt(clist[2]);
          } else {
            this.class_name_3_new = "";
          }
          if (clist[3]) {
            this.class_name_4_new = parseInt(clist[3]);
          } else {
            this.class_name_4_new = "";
          }
          if (clist[4]) {
            this.class_name_5_new = parseInt(clist[4]);
          } else {
            this.class_name_5_new = "";
          }
          if (clist[5]) {
            this.class_name_6_new = parseInt(clist[5]);
          } else {
            this.class_name_6_new = "";
          }
          if (clist[6]) {
            this.class_name_7_new = parseInt(clist[6]);
          } else {
            this.class_name_7_new = "";
          }
          if (clist[7]) {
            this.class_name_8_new = parseInt(clist[7]);
          } else {
            this.class_name_8_new = "";
          }
          if (clist[8]) {
            this.class_name_9_new = parseInt(clist[8]);
          } else {
            this.class_name_9_new = "";
          }
          this.courseid_updated = row.course_id;
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleDelete(index, row) {
      this.$confirm("确定要删除这条课程数据吗？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.axios.get("/course/remove/" + row.course_id).then(response => {
            var resp = response.data;
            this.$message({
              message: resp["infomsg"]
            });
            this.getData();
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleAdd() {
      var classliststr =
        this.class_name_1 +
        "," +
        this.class_name_2 +
        "," +
        this.class_name_3 +
        "," +
        this.class_name_4 +
        "," +
        this.class_name_5 +
        "," +
        this.class_name_6 +
        "," +
        this.class_name_7 +
        "," +
        this.class_name_8 +
        "," +
        this.class_name_9;
      this.axios
        .post("/course/", {
          course_name: this.course_name,
          course_isgroup: this.course_isgroup,
          course_classlist: classliststr
        })
        .then(response => {
          var resp = response.data;
          this.$message({
            message: resp["infomsg"]
          });
          this.getData();
          this.course_name = "";
          this.course_isgroup = "0";
          this.class_name_1 = "";
          this.class_name_2 = "";
          this.class_name_3 = "";
          this.class_name_4 = "";
          this.class_name_5 = "";
          this.class_name_6 = "";
          this.class_name_7 = "";
          this.class_name_8 = "";
          this.class_name_9 = "";
          document.getElementById("crname").focus();
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>
