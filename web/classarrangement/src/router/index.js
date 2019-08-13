import Vue from 'vue'
import Router from 'vue-router'
import Navigator from '@/components/Navigator'
import Classroom from '@/components/Classroom'
import Teacher from '@/components/Teacher'
import Class1 from '@/components/Class1'
import Course from '@/components/Course'
import Courseplan from '@/components/Courseplan'
import Arrangement from '@/components/Arrangement'
import Info from '@/components/Info'
import Showdetailtable from '@/components/Showdetailtable'
import Change from '@/components/Change'

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'classroom',
      component: Classroom
    }, {
      path: '/teacher',
      name: 'teacher',
      component: Teacher
    }, {
      path: '/class1',
      name: 'class1',
      component: Class1
    }, {
      path: '/course',
      name: 'course',
      component: Course
    }, {
      path: '/courseplan',
      name: 'courseplan',
      component: Courseplan
    }, {
      path: '/arrangement',
      name: 'arrangement',
      component: Arrangement
    }, {
      path: '/info',
      name: 'info',
      component: Info
    }, {
      path: '/showdetailtable',
      name: 'showdetailtable',
      component: Showdetailtable
    }, {
      path: '/change',
      name: 'change',
      component: Change
    }
  ]
})
