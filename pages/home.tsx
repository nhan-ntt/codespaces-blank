/* eslint-disable react-hooks/exhaustive-deps */
import type { NextPage } from "next";

import AppLayout from "@/layouts/appLayout";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { Artists } from "../interfaces/artist";
import {
    getRecentUsers,
    HomePageState,
    RequestStatus,
} from "../stores/homePage/homePageSlice";
import CustomImage from "../components/CustomImage";
import HorizontalSongsList from "../components/HorizontalSongsList";
import HorizontalArtistsList from "../components/HorizontalArtistsList";
import { useRouter } from "next/router";
import ErrorComponent from "@/components/error";
import { getGreetings } from "@/configs/utils";

const Home: NextPage = () => {
    const {
        recentUsers: recentArtist,
        status,
        topHits,
        popularHits,
        trendingArtists,
    }: HomePageState = useSelector((state: any) => state.homePage);
    const { user } = useSelector((state: any) => state.auth);

    const dispatch = useDispatch<any>();
    const [color, setColor] = useState("#2bb540");
    const router = useRouter();

    useEffect(() => {
        if (user) {
            if (status !== RequestStatus.Success) {
                dispatch(getRecentUsers());
            }

            if (status == RequestStatus.Success) {
                setColor("black");
            }
        }
    }, []);

    return (
        <AppLayout title="Home" color={color}>
            {status == RequestStatus.Loading ? (
                <div
                    className=" w-[calc(100vw_-_14rem_-_16px)] mini-laptop:w-[calc(100vw_-_55px)] 
        tablet:w-screen mobile:w-screen overflow-x-hidden  h-screen mobile:h-[calc(100vh_-_50px)] 
        tablet:h-[calc(100vh_-_50px)] flex flex-col items-center justify-center"
                >
                    <span className="loader"></span>
                    <p className="text-sm text-white my-3 font-ProximaRegular">
                        Loading...
                    </p>
                </div>
            ) : status == RequestStatus.Error ? (
                <ErrorComponent />
            ) : status == RequestStatus.Success ? (
                <div className="pt-10 mini-laptop:pt-2 mobile:pt-1 tablet:pt-2">
                    <h1 className="select-none pt-6 tablet:px-6 px-8 mobile:px-4 pb-6 text-3xl font-ProximaBold mini-laptop:text-2xl tablet:text-2xl mobile:text-xl">
                        {getGreetings()}
                    </h1>
                    <div
                        className="select-none px-8 tablet:px-6 mobile:px-4 grid grid-cols-3 gap-x-6 gap-y-5 mini-laptop:gap-x-3 
          mini-laptop:gap-y-4 tablet:gap-y-4 tablet:gap-x-3 mobile:grid-cols-2 mobile:gap-x-3 mobile:gap-y-3"
                    >
                        {recentArtist.map((artist: Artists) => (
                            <div
                                key={artist.id}
                                onClick={() =>
                                    router.push(`/artist/${artist.id}`)
                                }
                                onMouseEnter={() => setColor("black")}
                                onMouseLeave={() => setColor("black")}
                                className="flex flex-row items-center
                      font-ProximaBold w-full bg-[#5f5d5d60]
                      rounded-md cursor-pointer hover:bg-[#5f5d5da1]"
                            >
                                <div
                                    style={{
                                        backgroundColor: "black",
                                        boxShadow:
                                            "10px 0 10px -7px rgba(18, 18, 18, 0.50), -0px 0 0px -4px rgba(0, 0, 0, 0)",
                                    }}
                                    className="relative w-20 h-20 mini-laptop:w-16 mini-laptop:h-16
                        rounded-tl-md rounded-bl tablet:w-16 tablet:h-16 mobile:w-14 mobile:h-14"
                                >
                                    <CustomImage
                                        src={
                                            "https://images3.alphacoders.com/690/690494.jpg&auto=format&fit=crop&w=200&q=50&h=200"
                                        }
                                        className="rounded-tl rounded-bl shadow-2xl shadow-black"
                                    />
                                </div>
                                <p className="p-4 mini-laptop:p-2 tablet:p-2 tablet:text-[15px] mobile:p-0 mobile:px-2 mobile:text-[14px]">
                                    {artist.name}
                                </p>
                            </div>
                        ))}
                    </div>
                    <div className="mt-12">
                        <h1 className="px-8 tablet:px-6 mobile:px-4 text-xl font-ProximaBold mb-6 mobile:text-base">
                            Trending Artists
                        </h1>
                        <HorizontalArtistsList artists={trendingArtists} />
                    </div>

                    <div className="mt-12">
                        <h1 className="px-8 tablet:px-6 mobile:px-4 text-xl font-ProximaBold mb-6 mobile:text-base">
                            Top Hits this Week
                        </h1>
                        <HorizontalSongsList songs={topHits} />
                    </div>
                    <div className="mt-6">
                        <h1 className="px-8 tablet:px-6 mobile:px-4 text-xl font-ProximaBold mb-6 mobile:text-base">
                            Popular releases
                        </h1>
                        <HorizontalSongsList songs={popularHits} />
                    </div>
                    <div className="h-40"></div>
                </div>
            ) : (
                <div className="w-full h-screen"></div>
            )}
        </AppLayout>
    );
};

export default Home;
