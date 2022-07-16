import React from 'react';
import ReactDOM from 'react-dom';
// import ReactDOM from "react-dom/client";
import './index.css';
import App from './App';
// import reportWebVitals from './reportWebVitals';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import Register from './components/auth/register';
import Login from './components/auth/login';
import Logout from './components/auth/logout';
import Single from './components/posts/single';
import Search from './components/posts/search';
import Admin from './Admin';
import Create from './components/admin/create';
import Edit from './components/admin/edit';
import Delete from './components/admin/delete';




// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );



const routing = (
	<Router>
		<React.StrictMode>
			<Header />
			<Switch>
			<Route exact path="/" component={App} />
				<Route exact path="/admin" component={Admin} />
				<Route exact path="/admin/create" component={Create} />
				<Route exact path="/admin/edit/:id" component={Edit} />
				<Route exact path="/admin/delete/:id" component={Delete} />
				<Route path="/register" component={Register} />
				<Route path="/login" component={Login} />
				<Route path="/logout" component={Logout} />
				<Route path="/post/:slug" component={Single} />
				<Route path="/search" component={Search} />
			</Switch>
			<Footer />
		</React.StrictMode>
	</Router>
);

ReactDOM.render(routing, document.getElementById('root'));
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
