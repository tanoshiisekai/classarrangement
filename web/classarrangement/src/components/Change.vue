<template>
  <div class="container">
    <Navigator defaultActive="change"></Navigator>
    <el-row>
      <el-col :span="6" :gutter="20" :offset="9">
        <el-select v-model="class1" filterable placeholder="请选择班级" style="width:480px;">
          <el-option
            v-for="item in classlist"
            :key="item.class_id"
            :label="item.class_name"
            :value="item.class_id"
          ></el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row  style="margin-top: 50px;">
      <el-col :span="2" :gutter="20" :offset="7">
        <el-select v-model="week1" filterable placeholder="请选择星期" style="width:160px;">
          <el-option v-for="item in weeklist" :key="item" :label="item" :value="item"></el-option>
        </el-select>
      </el-col>
      <el-col :span="2" :gutter="20">
        <el-select v-model="section1" filterable placeholder="请选择节次" style="width:160px;">
          <el-option v-for="item in sectionlist" :key="item" :label="item" :value="item"></el-option>
        </el-select>
      </el-col>
      <el-col :span="2">
        <i
          class="el-icon-sort"
          name="el-icon-sort"
          style="font-size:36px;font-weight:bold;transform: rotate(90deg);x;"
        ></i>
      </el-col>
      <el-col :span="2" :gutter="20">
        <el-select v-model="week2" filterable placeholder="请选择星期" style="width:160px;">
          <el-option v-for="item in weeklist" :key="item" :label="item" :value="item"></el-option>
        </el-select>
      </el-col>
      <el-col :span="2" :gutter="20">
        <el-select v-model="section2" filterable placeholder="请选择节次" style="width:160px;">
          <el-option v-for="item in sectionlist" :key="item" :label="item" :value="item"></el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row style="margin-top: 50px;">
      <el-col :span="2" :offset="10">
        <el-button type="primary" style="width: 200px;margin-left:50px;" @click="handleChange()">调课</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Navigator from "@/components/Navigator";
export default {
  name: "change",
  components: {
    Navigator
  },
  created() {
    this.getclasslist();
  },
  data() {
    return {
      class1: "",
      class2: "",
      week1: "",
      week2: "",
      section1: "",
      section2: "",
      classlist: [],
      weeklist: ["一", "二", "三", "四", "五", "六", "日"],
      sectionlist: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    };
  },
  methods: {
    handleChange() {
      console.log(this.class1);
      console.log(this.class2);
      console.log(this.week1);
      console.log(this.week2);
      console.log(this.section1);
      console.log(this.section2);
      this.class2 = this.class1;
      this.axios
        .get(
          "/arrangement/" +
            this.class1 +
            "/" +
            this.week1 +
            "/" +
            this.section1 +
            "/" +
            this.class2 +
            "/" +
            this.week2 +
            "/" +
            this.section2
        )
        .then(response => {
          var resp = response.data;
          if (resp["infostatus"]) {
            this.$message({
              message: resp["infomsg"]
            });
          } else {
            this.$message({
              message: resp["infomsg"],
              duration: 0,
              showClose: true,
              type: "error"
            });
          }
        });
    },
    getclasslist() {
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
    }
  }
};
</script>

<style>
.container {
  margin-top: 100px;
}
</style>
