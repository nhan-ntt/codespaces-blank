/* eslint-disable react-hooks/exhaustive-deps */
import type { NextPage } from "next";
import { useRouter } from "next/navigation";
import { useSelector } from "react-redux";
import { useEffect } from "react";

import { Link, Button, Image } from "@nextui-org/react";
import Head from "next/head";

export async function getServerSideProps(ctx: any) {
    const token = ctx.req.cookies.user;
    if (token) {
        return {
            redirect: {
                destination: `/home`,
                permanent: false,
            },
        };
    }

    return {
        props: {},
    };
}

const Home: NextPage = () => {
    const { status, user } = useSelector((state: any) => state.auth);
    const router = useRouter();
    useEffect(() => {
        if (user) {
            router.push("/home");
        }
    }, [router, user, status]);

    return (
        <div className="font-ProximaRegular bg-[#0d0d0d] text-white">
            <Head>
                <meta
                    property="og:title"
                    content="Rhyme - Download & use free music anywhere."
                />
                <meta
                    property="og:site_name"
                    content="Rhyme - Download & use free music anywhere."
                />
                <meta property="og:url" content="https://Rhyme.vercel.app" />

                <meta
                    property="og:description"
                    content="Explore & download free stock music and use it anywhere you like
            with spotify web player experience."
                />

                <meta
                    property="og:image"
                    itemProp="image"
                    content="https://Rhyme.vercel.app/Rhyme_intro_card.png"
                />

                <meta property="og:type" content="article" />
                <meta name="twitter:card" content="summary_large_image" />
                <meta name="twitter:site" content="Rhyme.vercel.app" />
                <meta name="twitter:creator" content="@AnshhRathod" />
                <meta
                    name="twitter:title"
                    content="Rhyme - Download & use free music anywhere."
                />
                <meta
                    name="twitter:description"
                    content="Explore & download free stock music and use it anywhere you like
            with spotify web player experience."
                />
                <meta
                    name="twitter:image"
                    itemProp="image"
                    content="https://Rhyme.vercel.app/Rhyme_intro_card.png"
                />
                <title>Rhyme - Free music anywhere.</title>
            </Head>

            <div className="fixed top-0 left-0 right-0 z-40 bg-[#0d0d0d]">
                <div className="flex flex-row max-w-[1280px] justify-between items-center mx-auto p-2">
                    <div className="flex flex-row items-center">
                        <Image
                            src="/logo.png"
                            width={40}
                            height={40}
                            alt="logo"
                        />
                        <h1
                            className="text-center uppercase mx-2 
              tracking-wider font-ProximaBold"
                        >
                            Rhyme
                        </h1>
                    </div>
                    <div className="flex gap-3 ">
                        <Button
                            variant="bordered"
                            className="text-bold text-sm"
                            onClick={() => router.push("/login")}
                        >
                            Login
                        </Button>
                        <Button
                            variant="bordered"
                            className="text-bold text-sm"
                            onClick={() => router.push("/register")}
                        >
                            Register
                        </Button>
                    </div>
                </div>
            </div>

            <div className="relative">
                <div
                    className="overflow-hidden pt-36 pb-20 mobile:pb-16  w-full 
        flex justify-center items-center "
                >
                    <div
                        className="cliped w-[600px] h-[300px] bg-[#2bb540]
          bg-gradient-to-r from-[#2bb] via-[#2bb540] to-yellow-200
           bg-opacity-80"
                    ></div>
                </div>
                <div
                    className="bg-[#0d0d0d] bg-opacity-30 pt-36 pb-20 mobile:pb-16 
          backdrop-blur-[70px] 
        absolute z-10 inset-0 max-w-[1280px] mx-auto 
         flex justify-center flex-col items-center"
                >
                    <h1
                        className="text-[70px] font-ProximaBold text-center
           leading-[5rem] mini-laptop:text-[60px] tablet:text-[50px] mini-laptop:leading-[4rem]
            tablet:leading-[4rem] mobile:text-[35px] mobile:leading-[2.5rem]"
                    >
                        Free Music anywhere!
                    </h1>
                    <p className="text-center mt-4 max-w-[600px] mx-auto text-[18px] px-8">
                        Explore & download free stock music
                    </p>
                    <Button
                        className="cursor-pointer shadow-md px-5 py-2 rounded-3xl font-bold text-lg mt-6 bg-[#2bb540] w-fit"
                        onClick={() => router.push("/register")}
                    >
                        Get started
                    </Button>
                </div>
            </div>
            <div>
                <div
                    className=" bg-[#0d0d0d]  backdrop-blur-[50px] 
      max-w-[1280px] mx-auto mobile:hidden"
                >
                    <div className="max-w-[1000px] mx-auto">
                        <Image
                            src={"/landing_page.png"}
                            width="1000"
                            height="500"
                        />
                    </div>
                </div>
                <div className="overflow-hidden pl-10">
                    <div className="hidden mobile:block relative h-[400px] w-[600px]">
                        <Image src={"/landing_page.png"} className="rounded" />
                    </div>
                </div>
            </div>

            <div className="max-w-[1000px] mx-auto">
                <h1 className="text-center text-3xl font-ProximaBold mt-10 mb-10">
                    Features
                </h1>

                <div
                    className="grid grid-cols-3 gap-4 mini-laptop:grid-cols-2 px-6
        tablet:grid-cols-1 mobile:grid-cols-1
        "
                >
                    <div
                        className="bg-gradient-to-tr to-[#a15c1c] 
          from-[#6a2009] py-4 px-6 rounded flex text-center 
          flex-col  items-center"
                    >
                        <div className="mb-4 mt-3 bg-[#2ed146] w-fit p-3 rounded-full text-center flex items-center">
                            <i className="icon-full-screen text-[20px]"></i>
                        </div>

                        <h1 className="text-xl font-ProximaBold mb-2 ">
                            Fully Responsive
                        </h1>
                        <p>
                            Available for all screen Mobile, tablet, laptop and
                            desktop. The app is made to give a user full
                            experience of spotify client. it has almost same Ui
                            as Spotify for every page.
                        </p>
                    </div>
                    <div
                        className="bg-gradient-to-b from-[#8b0847] 
          to-[#580b64] py-4 px-6 rounded flex text-center 
          flex-col  items-center"
                    >
                        <div className="mb-4 mt-3 bg-[#2ed146] w-fit p-3 rounded-full text-center flex items-center">
                            <i className="icon-add-to-playlist text-[20px]"></i>
                        </div>

                        <h1 className="text-xl font-ProximaBold mb-2 ">
                            Different Themes
                        </h1>
                        <p>
                            Stock music with variety of themes. Music for
                            videos, Music for youtube videos, Vlog music
                            Background, Film music, Podcast music, Cinematic
                            music and much more.
                        </p>
                    </div>
                    <div
                        className="bg-gradient-to-tr to-[#0d2477] 
          from-[#522bbf] py-4 px-6 rounded flex text-center
           flex-col items-center"
                    >
                        <div className="mb-4 mt-3 bg-[#2ed146] w-fit p-3 rounded-full text-center flex items-center">
                            <i className="icon-verified text-[24px]"></i>
                        </div>

                        <h1 className="text-xl font-ProximaBold mb-2 ">
                            Safe to use
                        </h1>
                        <p>
                            Over 10k+ high quality stock music, shared by
                            community of pixabay music. safe to use without
                            asking for permission or giving credit to the artist
                            - even for commercial purposes.
                        </p>
                    </div>
                </div>
                <div
                    className="mt-10  py-10 border-t 
         items-center flex flex-col border-t-slate-800"
                ></div>
            </div>
        </div>
    );
};

export default Home;
