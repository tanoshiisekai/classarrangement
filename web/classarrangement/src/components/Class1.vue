<template>
  <div class="container">
    <Navigator defaultActive="class1"></Navigator>
    <el-row :gutter="20" style="margin:10px;">
      <el-col :span="6">
        <el-input v-model="class_name" placeholder>
          <template slot="prepend">班级名称</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-select v-model="teacherselected" filterable placeholder="请选择班主任">
          <el-option
            v-for="item in teacherlist"
            :key="item.teacher_id"
            :label="item.teacher_name"
            :value="item.teacher_id"
          ></el-option>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-select v-model="classroomselected" filterable placeholder="请选择教室">
          <el-option
            v-for="item in classroomlist"
            :key="item.classroom_id"
            :label="item.classroom_name"
            :value="item.classroom_id"
          ></el-option>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" class="mybutton" @click="this.handleAdd">添加</el-button>
      </el-col>
    </el-row>
    <el-row style="margin:30px;">
      <el-col :span="24">
        <el-table :data="classlist" style="width: 100%">
          <el-table-column label="班级名称">
            <template slot-scope="scope">{{scope.row.class_name}}</template>
          </el-table-column>
          <el-table-column label="班主任">
            <template slot-scope="scope">{{scope.row.teacher_name}}</template>
          </el-table-column>
          <el-table-column label="默认教室">
            <template slot-scope="scope">{{scope.row.classroom_name}}</template>
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
    <el-dialog title="编辑班级信息" :visible.sync="updatedialog">
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">班级名称</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="class_name_new" class="samelengthwithselect">
          </el-input>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">班主任</el-tag>
        </el-col>
        <el-col :span="14">
          <el-select v-model="teacher_id_new" filterable placeholder="请选择班主任"  class="samelengthwithselect">
            <el-option
              v-for="item in teacherlist"
              :key="item.teacher_id"
              :label="item.teacher_name"
              :value="item.teacher_id"
            ></el-option>
          </el-select>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">默认教室</el-tag>
        </el-col>
        <el-col :span="14">
          <el-select v-model="classroom_id_new" filterable placeholder="请选择教室" class="samelengthwithselect">
          <el-option
            v-for="item in classroomlist"
            :key="item.classroom_id"
            :label="item.classroom_name"
            :value="item.classroom_id"
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
  name: "class1",
  components: {
    Navigator
  },
  data() {
    return {
      teacherlist: [],
      classroomlist: [],
      teacherselected: "",
      classroomselected: "",
      class_name: "",
      classlist: [],
      class_name_new: "",
      teacher_id_new: "",
      classroom_id_new: "",
      classid_updated: "",
      updatedialog: false
    };
  },
  created() {
    this.getTeacherList();
    this.getClassroomList();
    this.getData();
  },
  methods: {
    getData() {
      this.axios.get("/class/details/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.classlist = resp["inforesult"];
          this.classlist.sort((a, b)=>{return b['class_id']-a['class_id']});
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
          this.teacherlist.sort((a, b)=>{return a['teacher_name']>b['teacher_name']});
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
          this.classroomlist.sort((a, b)=>{return a['classroom_name']-b['classroom_name']});
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleAdd() {
      this.axios
        .post("/class/", {
          class_name: this.class_name,
          teacher_id: this.teacherselected,
          classroom_id: this.classroomselected
        })
        .then(response => {
          var resp = response.data;
          this.$message({
            message: resp["infomsg"]
          });
          this.getData();
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleUpdate(index, row) {
      this.updatedialog = true;
      this.axios.get("/class/" + row.class_id).then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          var redata = resp["inforesult"];
          this.class_name_new = redata["class_name"];
          this.teacher_id_new = redata["teacher_id"];
          this.classroom_id_new= redata["classroom_id"];
          this.classid_updated = row.class_id;
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleSubUpdate() {
      this.axios
        .post("/class/update/" + this.classid_updated, {
          class_name: this.class_name_new,
          teacher_id: this.teacher_id_new,
          classroom_id: this.classroom_id_new
        })
        .then(response => {
          var resp = response.data;
          this.$message({
            message: resp["infomsg"]
          });
          this.updatedialog = false;
          this.getData();
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleDelete(index, row) {
      this.$confirm("确定要删除这条班级数据吗？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.axios.get("/class/remove/" + row.class_id).then(response => {
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
    }
  }
};
</script>

<style>
</style>
