import {useEffect, useState} from "react";
import {getSolverByPattern} from "../../controllers/rubick.controller.jsx";
import {useForm} from "react-hook-form";

function Rubick(){
    const {handleSubmit, register} = useForm({
        defaultValues:{
            pattern:''
        }
    });
    const [data,setData] = useState(null)
    const solveMatrix=(value)=>{
        /*console.log(value)*/
        const x=value.split('\n')
        /*console.log(x)*/
        return x.map(item=>{
            return <span className={"d-flex justify-content-center"}>{item}</span>
        })
    }

    const onSubmit = async (data) => {
        console.log("data", data)
        const response = await getSolverByPattern(data)
        setData(response)
    }
    return (
        <>
            <main className="container-fluid">
                <h2>Implementación del Algoritmo de Korf para la Solución Óptima del Cubo Rubik</h2>
                <section>
                    <form onSubmit={handleSubmit(onSubmit)}>
                        <div className="my-5">
                            <div className="d-flex justify-content-center">
                                <label htmlFor="rubick" className="col-form-label me-2 me-md-4 fw-bold">Patron:</label>
                                <div className="contact__form-input">
                                    <input style={{width:'600px'}} type="text"
                                           name="rubick" {...register('pattern')}/>
                                </div>
                            </div>
                        </div>
                        <div className="my-5 d-flex justify-content-center">
                            <button type="submit" className="btn btn-info">Enviar</button>
                        </div>
                    </form>
                </section>
                { data? <section className={"container"}>
                    <section className={"mt-5"}>
                        <div>
                            {solveMatrix(data.d1.l1)}
                        </div>
                        <div>
                            {solveMatrix(data.d1.l2)}
                        </div>
                        <div>
                            {solveMatrix(data.d1.l3)}
                        </div>
                    </section>
                    {/*<hr className={"my-5"}/>
                    <section className={"mt-5"}>
                        <div>
                            {solveMatrix(data.d2.l1)}
                        </div>
                        <div>
                            {solveMatrix(data.d2.l2)}
                        </div>
                        <div>
                            {solveMatrix(data.d2.l3)}
                        </div>
                    </section>*/}
                    <hr className={"my-5"}/>
                    <section className={"d-flex flex-column"}>
                       <p>Movimientos: {JSON.stringify(data.move)}</p>
                        <p>Tiempo en resolver el cubo  (s): {data.time}</p>
                    </section>
                    <section className="mt-5">
                        <div>
                            {solveMatrix(data.d3.l1)}
                        </div>
                        <div>
                            {solveMatrix(data.d3.l2)}
                        </div>
                        <div>
                            {solveMatrix(data.d3.l3)}
                        </div>
                    </section>
                </section> : <p>resolviendo</p>}
            </main>
        </>
    )
}

export default Rubick
