baseURL = "http://127.0.0.1:5000/api/cupcakes"


//// How school did it 
// function generateCupcakeHTML(cupcake) {
//     return `
//       <div data-cupcake-id=${cupcake.id}>
//         <li>
//           ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
//           <button class="delete-button">X</button>
//         </li>
//         <img class="Cupcake-img"
//               src="${cupcake.image}"
//               alt="(no image provided)">
//       </div>
//     `;
//   }

// async function showInitialCupcakes() {
//     const response = await axios.get(`${BASE_URL}/cupcakes`);
  
//     for (let cupcakeData of response.data.cupcakes) {
//       let newCupcake = $(generateCupcakeHTML(cupcakeData));
//       $("#cupcakes-list").append(newCupcake);
//     }
//   }

$('.delete-Cupcake').click(deleteCupcake)

async function deleteCupcake() {
  const id = $(this).data('id')
  await axios.delete(`/api/cupcakes/${id}`)
  $(this).parent().remove()
}





/** handle form for adding of new cupcakes */

// $("#new-cupcake-form").on("submit", async function (evt) {
//     evt.preventDefault();
  
//     let flavor = $("#form-flavor").val();
//     let rating = $("#form-rating").val();
//     let size = $("#form-size").val();
//     let image = $("#form-image").val();
  
//     const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
//       flavor,
//       rating,
//       size,
//       image
//     });
  
//     let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
//     $("#cupcakes-list").append(newCupcake);
//     $("#new-cupcake-form").trigger("reset");
//   });
  
  
//   /** handle clicking delete: delete cupcake */
  
//   $("#cupcakes-list").on("click", ".delete-button", async function (evt) {
//     evt.preventDefault();
//     let $cupcake = $(evt.target).closest("div");
//     let cupcakeId = $cupcake.attr("data-cupcake-id");
  
//     await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
//     $cupcake.remove();
//   });
  
  
//   $(showInitialCupcakes);



// what is cupcake response.data.cupcake ?
// I saw the solution but Why is my delete button not working? 
//My post request not working, there is always keyType error problem? 
//request.json turns red when being used but it is not working any more(app.py)
//my test I can not run, I saw a video on how to run a test on VS code but still not running(tests.py)
// my PATCH route is not working either
// Do i have to use JS to add a new cupcake? if not would I just use request.form
//can't find a youtube video on request.json(do developers not use it ?) 
