import { useState } from 'react';
import { loginAction } from '../../redux/auth.slice';
import { useNavigate, Navigate, Link } from 'react-router-dom';
import { IsError } from '../../components/ISError';
import { LoadingIndicator } from '../../components/Loading';
import { useDispatch, useSelector } from 'react-redux';

export default function Login() {
  const [email, setEmail] = useState('');
  const navigate = useNavigate();
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();
  const { loading, error, user } = useSelector((state) => state.authReducer);

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();

    formData.append('username', email);
    formData.append('password', password);

    dispatch(loginAction(formData));

    navigate('/');
  };

  if (user) {
    return <Navigate to={'/'} />;
  }

  return (
    <>
      {loading ? (
        <LoadingIndicator />
      ) : error ? (
        <>
          <IsError error={error} />
        </>
      ) : (
        <>
          <div className="flex justify-center items-center mt-20">
            <div className="w-full max-w-md ">
              <div className="bg-white shadow-lg p-6 rounded-lg">
                <h2 className="text-center text-2xl font-semibold mb-6">
                  LOGIN
                </h2>
                <i className="fa fa-sign-in text-3xl mb-6 mx-auto"></i>

                <form onSubmit={handleSubmit}>
                  <input
                    type="text"
                    placeholder="Email"
                    className="w-full p-2 mb-4 border border-gray-300 rounded"
                    value={email}
                    required
                    onChange={(e) => setEmail(e.target.value)}
                  />

                  <input
                    type="password"
                    placeholder="Password"
                    className="w-full p-2 mb-4 border border-gray-300 rounded"
                    value={password}
                    required
                    onChange={(e) => setPassword(e.target.value)}
                  />

                  <div className="text-right">
                    <button
                      type="submit"
                      className="bg-blue-500 text-white px-4 py-2 rounded"
                    >
                      LOGIN
                    </button>
                  </div>
                </form>

                <Link to="/register" className="block mt-4 text-center">
                  Click Here To Register
                </Link>
              </div>
            </div>
          </div>
        </>
      )}
    </>
  );
}
