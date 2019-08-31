<template>
  <div class="container">
    <Navigator defaultActive="teacherarrangement"></Navigator>
    <el-row>
      <el-select v-model="teacherid" filterable placeholder="请选择老师" style="width:500px;">
        <el-option
          v-for="item in teacherlist"
          :key="item.teacher_id"
          :label="item.teacher_name"
          :value="item.teacher_id"
        ></el-option>
      </el-select>
      <el-button
        type="info"
        class="mybutton"
        @click="handleQuery()"
        style="width:150px;margin-left:20px;"
      >查询</el-button>
    </el-row>
    <el-row style="margin-top:50px;">
      <vxe-table :data.sync="tabledatalist" border resizable stripe>
        <vxe-table-column type="index" width="100"></vxe-table-column>
        <vxe-table-column field="monday" title="一" width="200"></vxe-table-column>
        <vxe-table-column field="tuesday" title="二" width="200"></vxe-table-column>
        <vxe-table-column field="wednesday" title="三" width="200"></vxe-table-column>
        <vxe-table-column field="thirsday" title="四" width="200"></vxe-table-column>
        <vxe-table-column field="friday" title="五" width="200"></vxe-table-column>
        <vxe-table-column field="saturday" title="六" width="200"></vxe-table-column>
        <vxe-table-column field="sunday" title="日" width="200"></vxe-table-column>
      </vxe-table>
    </el-row>
  </div>
</template>

<script>
import Navigator from "@/components/Navigator";
export default {
  name: "teacherarrangement",
  components: {
    Navigator
  },
  created() {
    this.getTeacherList();
  },
  data() {
    return {
      tabledatalist: [
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        }
      ],
      teacherid: "",
      teacherlist: [],
      weeklist: ["一", "二", "三", "四", "五", "六", "日"],
      sectionlist: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    };
  },
  methods: {
    getTeacherList() {
      this.axios.get("/teacher/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.teacherlist = resp["inforesult"];
          this.teacherlist.sort((a, b) => {
            return b["teacher_id"] - a["teacher_id"];
          });
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    },
    handleQuery() {
      this.tabledatalist = [
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        }
      ];
      var teacherid = this.teacherid;
      this.axios.get("/arrangement/teacher/" + teacherid).then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          var result = resp["inforesult"];
          for (var i in result) {
            console.log(result[i]);
            var weekname = "";
            var wname = result[i]["arrangement_week"];
            if (wname == "一") {
              weekname = "monday";
            } else if (wname == "二") {
              weekname = "tuesday";
            } else if (wname == "三") {
              weekname = "wednesday";
            } else if (wname == "四") {
              weekname = "thirsday";
            } else if (wname == "五") {
              weekname = "friday";
            } else if (wname == "六") {
              weekname = "saturday";
            } else if (wname == "日") {
              weekname = "sunday";
            }
            var sectionname = parseInt(result[i]["arrangement_section"]) - 1;
            var classname = result[i]["class_name"];
            var coursename = result[i]["course_name"];
            this.tabledatalist[sectionname][weekname] =
              coursename + " - -【" + classname + "】";
          }
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
