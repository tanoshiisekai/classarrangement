<template>
  <div class="container">
    <Navigator defaultActive="teacher"></Navigator>
    <el-row :gutter="20" style="margin:10px;">
      <el-col :span="6">
        <el-input v-model="teacher_name" placeholder id="tname">
          <template slot="prepend">教师姓名</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-input v-model="teacher_mobile" placeholder>
          <template slot="prepend">手机号</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-input v-model="teacher_request" placeholder>
          <template slot="prepend">可以上课的时间</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" class="mybutton" @click="this.handleAdd">添加</el-button>
      </el-col>
    </el-row>
    <el-row style="margin:30px;">
      <el-col :span="24">
        <el-table :data="teacherlist" style="width: 100%">
          <el-table-column label="教师姓名">
            <template slot-scope="scope">{{scope.row.teacher_name}}</template>
          </el-table-column>
          <el-table-column label="手机号">
            <template slot-scope="scope">{{scope.row.teacher_mobile}}</template>
          </el-table-column>
          <el-table-column label="可以上课的时间">
            <template slot-scope="scope">{{scope.row.teacher_request}}</template>
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
    <el-dialog title="编辑教师信息" :visible.sync="updatedialog">
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">教师姓名</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="teacher_name_new" placeholder></el-input>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">手机号</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="teacher_mobile_new" placeholder></el-input>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">可以上课的时间</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="teacher_request_new" placeholder></el-input>
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
  name: "teacher",
  components: {
    Navigator
  },
  data() {
    return {
      teacher_name: "",
      teacher_mobile: "",
      teacher_request: "*@*",
      teacherlist: [],
      updatedialog: false,
      teacher_name_new: "",
      teacher_mobile_new: "",
      teacher_request_new: "",
      teacherid_updated: ""
    };
  },
  created() {
    var lett = this;
    document.onkeydown = function(e){
      var key = window.event.keyCode;
      if(key==13){
        lett.handleAdd();
      }
    }
    this.getData();
  },
  mounted() {
    document.getElementById("tname").focus();
  },
  methods: {
    getData() {
      this.axios.get("/teacher/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.teacherlist = resp["inforesult"];
          this.teacherlist.sort((a, b)=>{return b['teacher_id']-a['teacher_id']});
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleAdd() {
      this.axios
        .post("/teacher/", {
          teacher_name: this.teacher_name,
          teacher_mobile: this.teacher_mobile,
          teacher_request: this.teacher_request
        })
        .then(response => {
          var resp = response.data;
          this.$message({
            message: resp["infomsg"]
          });
          this.getData();
          this.teacher_name = "";
          this.teacher_mobile = "";
          document.getElementById("tname").focus();
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleUpdate(index, row) {
      this.updatedialog = true;
      this.axios.get("/teacher/" + row.teacher_id).then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          var redata = resp["inforesult"];
          this.teacher_name_new = redata["teacher_name"];
          this.teacher_mobile_new = redata["teacher_mobile"];
          this.teacher_request_new = redata["teacher_request"];
          this.teacherid_updated = row.teacher_id;
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleSubUpdate() {
      this.axios
        .post("/teacher/update/" + this.teacherid_updated, {
          teacher_name: this.teacher_name_new,
          teacher_mobile: this.teacher_mobile_new,
          teacher_request: this.teacher_request_new
        })
        .then(response => {
          var resp = response.data;
          this.$message({
            message: resp["infomsg"]
          });
          this.updatedialog = false;
          this.getData();
          this.teacher_name_new = "";
          this.teacher_mobile_new = "";
          this.teacher_request_new = "";
        })
        .catch(error => {
          console.log(error);
        });
    },
    handleDelete(index, row) {
      this.$confirm("确定要删除这条教师数据吗？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.axios.get("/teacher/remove/" + row.teacher_id).then(response => {
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
