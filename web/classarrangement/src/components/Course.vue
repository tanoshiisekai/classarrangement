<template>
  <div class="container">
    <Navigator defaultActive="course"></Navigator>
    <el-row :gutter="20" style="margin:10px;">
      <el-col :span="12">
        <el-input v-model="course_name" placeholder>
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
                <span v-if="scope.row.course_isgroup==1">
                是
                </span>
                <span v-else>
                否
                </span>
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
      course_isgroup: "",
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
      class_name_9: ""
    };
  },
  created() {
    this.getClassList();
    this.getData();
  },
  methods: {
    getData() {
        this.axios.get("/course/details/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.courselist = resp["inforesult"];
          this.courselist.sort((a, b)=>{return a['course_name']>b['course_name']});
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
    handleUpdate(index, row){

    },
    handleDelete(index, row){
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
