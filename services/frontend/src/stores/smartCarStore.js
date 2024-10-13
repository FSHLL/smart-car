import { algorithms } from "@/constants/algorithms";
import { defineStore } from "pinia";

export const useSmartCarStore = defineStore('smart-car', {
    state: () => ({
        matrix: [],
        matrixString: '',
        algorithm: [algorithms.UNINFORMED_BREADTH_SEARCH],
        solution: {}
    }),
})