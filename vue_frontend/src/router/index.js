import { createRouter, createWebHistory } from "vue-router";
import testView from "@/views/testView.vue";
import MainView from "@/views/MainView.vue";
import ArticleView from "@/views/ArticleView.vue";
import SignUpView from "@/views/SignUpView.vue";
import ProfileView from "@/views/ProfileView.vue";
import UserChart from "@/components/UserChart.vue";
import LogInView from "@/views/LogInView.vue";
import BankView from "@/views/BankView.vue";
import ExchangerView from "@/views/ExchangerView.vue";
import CreateArticle from "@/components/CreateArticle.vue";
import UpdateArticle from "@/components/UpdateArticle.vue";
import ArticleDetail from "@/components/ArticleDetail.vue";
import DepositsView from "@/views/DepositsView.vue";
import DepositDetail from "@/components/DepositDetail.vue";
import DepositOptions from "@/components/DepositOptions.vue";
import SavingsView from "@/views/SavingsView.vue";
import SavingDetail from "@/components/SavingDetail.vue";
import SavingOptions from "@/components/SavingOptions.vue";
import DepositGeneralRecommendationView from "@/views/DepositGeneralRecommendationView.vue";
import SavingGeneralRecommendationView from "@/views/SavingGeneralRecommendationView.vue";
import DepositClassifyView from "@/views/DepositClassifyView.vue";
import SavingClassifyView from "@/views/SavingClassifyView.vue";
import UpdateProfile from "../components/UpdateProfile.vue";
import UpdatePassword from '../components/UpdatePassword.vue';
import PersonalRecommendView from "@/views/PersonalRecommendView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/test",
      name: "testView",
      component: testView,
    },
    {
      path: "",
      name: "MainView",
      component: MainView,
    },
    {
      path: "/articles",
      name: "ArticleView",
      component: ArticleView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/exchanger",
      name: "ExchangerView",
      component: ExchangerView,
    },
    {
      path: "/bank",
      name: "BankView",
      component: BankView,
    },
    {
      path: "/article/create",
      name: "CreateArticle",
      component: CreateArticle,
    },
    {
      path: "/article/:id/update",
      name: "UpdateArticle",
      component: UpdateArticle,
    },
    {
      path: "/article/:id",
      name: "ArticleDetail",
      component: ArticleDetail,
    },
    {
      path: "/profile",
      name: "ProfileView",
      component: ProfileView,
    },
    {
      path: "/profile/update",
      name: "UpdateProfile",
      component: UpdateProfile,
    },
    {
      path: "/profile/chart",
      name: "UserChart",
      component: UserChart,
    },
    {
      path: "/password/update",
      name: "UpdatePassword",
      component: UpdatePassword,
    },
    {
      path: "/deposits",
      name: "DepositsView",
      component: DepositsView,
    },
    {
      path: "/deposits/:id",
      name: "DepositDetail",
      component: DepositDetail,
    },
    {
      path: "/deposits/options/:id",
      name: "DepositOptions",
      component: DepositOptions,
    },
    {
      path: "/savings",
      name: "SavingsView",
      component: SavingsView,
    },
    {
      path: "/savings/:id",
      name: "SavingDetail",
      component: SavingDetail,
    },
    {
      path: "/savings/options/:id",
      name: "SavingOptions",
      component: SavingOptions,
    },
    {
      path: "/depositgeneralrecommendation",
      name: "DepositGeneralRecommendationView",
      component: DepositGeneralRecommendationView,
    },
    {
      path: "/savinggeneralrecommendation",
      name: "SavingGeneralRecommendationView",
      component: SavingGeneralRecommendationView,
    },
    {
      path: "/depositclassify",
      name: "DepositClassifyView",
      component: DepositClassifyView,
    },
    {
      path: "/savingclassify",
      name: "SavingClassifyView",
      component: SavingClassifyView,
    },
    {
      path: "/personalrecommendiew",
      name: "PersonalRecommendView",
      component: PersonalRecommendView,
    },
  ],
});
import { useCounterStore } from "@/stores/counter";
import Swal from "sweetalert2";

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "ArticleView" && !store.isLogin) {
    Swal.fire({
      title: "로그인이 필요합니다",
      icon: "error",
      showConfirmButton: false,
      showDenyButton: true,
      denyButtonText: "확인",
      denyButtonColor: "#F27474",
    });
    return { name: "LogInView" };
  }
  if ((to.name === "SignUpView" || to.name === "LogInView") && store.isLogin) {
    Swal.fire({
      title: "이미 로그인된 사용자입니다",
      icon: "success",
      showConfirmButton: true,
      confirmButtonText: "확인",
      confirmButtonColor: "#a5dc86",
    });
    return { name: "ArticleView" };
  }
});

export default router;
