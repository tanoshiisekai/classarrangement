<template>
  <div class="container">
    <Navigator defaultActive="classroom"></Navigator>
    <el-row :gutter="20" style="margin:10px;">
      <el-col :span="6">
        <el-input v-model="classroom_name" placeholder>
          <template slot="prepend">教室名称</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-input v-model="classroom_position" placeholder>
          <template slot="prepend">教室位置</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-input v-model="classroom_available" placeholder>
          <template slot="prepend">可用时间</template>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" class="mybutton" @click="this.handleAdd">添加</el-button>
      </el-col>
    </el-row>
    <el-row style="margin:30px;">
      <el-col :span="24">
        <el-table :data="classroomlist" style="width: 100%">
          <el-table-column label="教室名称">
            <template slot-scope="scope">{{scope.row.classroom_name}}</template>
          </el-table-column>
          <el-table-column label="教室位置">
            <template slot-scope="scope">{{scope.row.classroom_position}}</template>
          </el-table-column>
          <el-table-column label="可用时间">
            <template slot-scope="scope">{{scope.row.classroom_available}}</template>
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
    <el-dialog title="编辑教室信息" :visible.sync="updatedialog">
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">教室名称</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="classroom_name_new" placeholder></el-input>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">教室位置</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="classroom_position_new" placeholder></el-input>
        </el-col>
      </el-row>
      <el-row style="margin:10px;">
        <el-col :span="6">
          <el-tag class="mylabel">可用时间</el-tag>
        </el-col>
        <el-col :span="14">
          <el-input v-model="classroom_available_new" placeholder></el-input>
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
  name: "classroom",
  components: {
    Navigator
  },
  data() {
    return {
      classroom_name: "",
      classroom_position: "",
      classroom_available: "",
      classroom_name_new: "",
      classroom_position_new: "",
      classroom_available_new: "",
      classroomid_updated: "",
      classroomlist: [],
      updatedialog: false
    };
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      this.classroomlist = [];
      this.classroom_name = "";
      this.classroom_position = "";
      this.classroom_available = "";
      this.axios.get("/classroom/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.classroomlist = resp["inforesult"];
          this.classroomlist.sort((a, b)=>{return a['classroom_name']>b['classroom_name']});
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleAdd() {
      this.axios
        .post("/classroom/", {
          classroom_name: this.classroom_name,
          classroom_position: this.classroom_position,
          classroom_available: this.classroom_available
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
      this.axios.get("/classroom/" + row.classroom_id).then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          var redata = resp["inforesult"];
          this.classroom_name_new = redata["classroom_name"];
          this.classroom_position_new = redata["classroom_position"];
          this.classroom_available_new = redata["classroom_available"];
          this.classroomid_updated = row.classroom_id;
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleSubUpdate() {
      this.axios
        .post("/classroom/update/" + this.classroomid_updated, {
          classroom_name: this.classroom_name_new,
          classroom_position: this.classroom_position_new,
          classroom_available: this.classroom_available_new
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
      this.$confirm("确定要删除这条教室数据吗？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.axios
            .get("/classroom/remove/" + row.classroom_id)
            .then(response => {
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
