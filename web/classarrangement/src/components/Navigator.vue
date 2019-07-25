<template>
  <div class="navigator">
    <el-menu
      :default-active="defaultActive"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="classroom">教室管理</el-menu-item>
      <el-menu-item index="teacher">教师管理</el-menu-item>
      <el-menu-item index="class1">班级管理</el-menu-item>
      <el-menu-item index="course">课程管理</el-menu-item>
      <el-menu-item index="courseplan">分课时管理</el-menu-item>
      <el-menu-item index="arrangement">排课管理</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "navigator",
  props: ["defaultActive"],
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
      if (key === "classroom") {
        this.$router.push({ name: "classroom" });
      } else if (key === "teacher") {
        this.$router.push({ name: "teacher" });
      } else if (key === "class1") {
        this.$router.push({ name: "class1" });
      } else if (key === "course") {
        this.$router.push({ name: "course" });
      } else if (key === "courseplan") {
        this.$router.push({ name: "courseplan" });
      } else if (key === "arrangement") {
        this.$router.push({ name: "arrangement" });
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>