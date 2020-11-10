<template>
    <div class="product">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
            <div class="container">
                <div class="row">
                <div v-for="product in APIData" :key="product.id" class="col-md-4">
                    <div class="card mb-4 box-shadow">
                    <!--
                    <img class="card-img-top" src="">{{product.image}}
                    <img :src="'/ressources/images/'+product.image">
                    <img class="card-img-top" v-bind:src="product.image" alt="Card image cap">
                    <img :src="product.image" />
                    <img :src="'lbj.jpeg'" :alt='product.name'>
                    <span>{{ product.image }}</span>
                    <img v-bind:src="product.image">-->
                    <div><img class="card-img-top" :src="getImgUrl(product.image)" v-bind:alt="product.image"></div>
                    <div class="card-body">
                        <h4 class=""><a class="text-secondary" href="">{{product.name}}</a></h4>
                        <p class="card-text">{{product.price}}</p>
                        <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                        <a href="" class="btn btn-sm btn-outline-primary" role="button" aria-pressed="true">-</a>
                        <a href="" class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">+</a>
                        </div>
                        <small class="text-muted">9 mins</small>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    export default {
        methods: {
            getImgUrl(imgName) {
                return require('.' + imgName)
            }
        },
        data1 () {
            return {
                object: {
                    image: 'image.png'
                }
            }
        },
        name: 'Product',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar
        },
        created () {
            getAPI.get('/product/',)
                .then(response => {
                    console.log('Post API has received data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>

<style scoped>

</style>